import streamlit as st
import requests

st.set_page_config(page_title="AI Planning Assistant", layout="wide")

st.title("AI Planning & Scheduling Assistant (MVP)")

st.markdown("Enter your tasks (one per line). Optional: add deadline using `| YYYY-MM-DD`")

raw_input = st.text_area(
    "Tasks",
    placeholder="Study AI | 2026-01-22\nPrepare exam"
)

available_minutes = st.number_input(
    "Available time today (minutes)",
    min_value=30,
    max_value=720,
    value=180,
    step=15
)

day = st.text_input("Day label", value="Today")

if st.button("Generate Plan"):
    if not raw_input.strip():
        st.error("Please enter at least one task.")
    else:
        tasks = []
        for line in raw_input.splitlines():
            if "|" in line:
                text, deadline = line.split("|", 1)
                tasks.append({
                    "text": text.strip(),
                    "deadline": deadline.strip()
                })
            else:
                tasks.append({"text": line.strip()})

        payload = {
            "tasks": tasks,
            "available_minutes": available_minutes,
            "day": day
        }

        with st.spinner("Planning..."):
            response = requests.post(
                "http://127.0.0.1:8000/plan",
                json=payload
            )

        if response.status_code != 200:
            st.error("API error. Is the server running?")
        else:
            data = response.json()

            st.subheader("1️⃣ Task Breakdown")
            for t in data["task_breakdown"]:
                st.write("-", t)

            st.subheader("2️⃣ Priority Table")
            st.table(
                {
                    "Task": [r[0] for r in data["priority_table"]],
                    "Priority": [r[1] for r in data["priority_table"]],
                    "Deadline": [r[2] for r in data["priority_table"]],
                    "Reason": [r[3] for r in data["priority_table"]],
                }
            )

            st.subheader("3️⃣ Schedule Plan")
            for b in data["schedule"]["blocks"]:
                st.write(
                    f"• {b['task']} — {b['duration_minutes']} min ({b['energy_fit']})"
                )

            st.subheader("4️⃣ Risk Flags")
            if data["risks"]:
                for r in data["risks"]:
                    st.warning(r)
            else:
                st.success("No major risks detected.")

            st.subheader("5️⃣ Next Actions")
            for a in data["next_actions"]:
                st.write("✅", a)
