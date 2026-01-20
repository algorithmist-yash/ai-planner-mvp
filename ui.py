import streamlit as st
import requests
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Daily Planner",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style="margin-bottom:0;">🗓️ Daily Planner</h1>
    <p style="color:gray;margin-top:0;">
    Plan your day realistically. Time-blocked. Risk-aware.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- INPUT SECTION ----------------
with st.container():
    st.subheader("📥 Task Inbox")

    raw_input = st.text_area(
        "",
        placeholder="Study AI | 2026-01-22\nPrepare exam | 2026-01-20\nWorkout",
        height=120
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        available_minutes = st.number_input(
            "Available time (minutes)",
            min_value=60,
            max_value=720,
            value=180,
            step=15
        )

    with col2:
        start_time = st.time_input(
            "Day start time",
            value=datetime.strptime("09:00", "%H:%M").time()
        )

    with col3:
        day = st.text_input("Day label", value="Today")

    generate = st.button("🧠 Generate Plan", use_container_width=True)

# ---------------- API CALL ----------------
if generate:
    if not raw_input.strip():
        st.error("Please enter at least one task.")
        st.stop()

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

    with st.spinner("Planning your day..."):
        response = requests.post(
            "http://api:8000/plan",
            json=payload
        )

    if response.status_code != 200:
        st.error("Planner API is not responding.")
        st.stop()

    data = response.json()

    st.divider()

    # ---------------- LAYOUT ----------------
    left, right = st.columns([1, 2])

    # ---------- LEFT: TASKS ----------
    with left:
        st.subheader("📋 Tasks")

        for row in data["priority_table"]:
            task, priority, deadline, reason = row
            badge = {
                "P1": "🔴",
                "P2": "🟠",
                "P3": "🟢"
            }.get(priority, "⚪")

            st.markdown(
                f"""
                <div style="padding:10px;border-radius:8px;
                border:1px solid #eee;margin-bottom:8px;">
                <b>{badge} {task}</b><br>
                <span style="color:gray;font-size:12px;">
                {reason}
                </span>
                </div>
                """,
                unsafe_allow_html=True
            )

    # ---------- RIGHT: SCHEDULE ----------
    with right:
        st.subheader("⏰ Time-Blocked Schedule")

        current_time = datetime.combine(
            datetime.today(),
            start_time
        )

        for block in data["schedule"]["blocks"]:
            end_time = current_time + timedelta(
                minutes=block["duration_minutes"]
            )

            st.markdown(
                f"""
                <div style="
                padding:14px;
                border-left:6px solid #4f8bf9;
                background:#f7f9fc;
                border-radius:8px;
                margin-bottom:10px;">
                <b>{current_time.strftime('%H:%M')} – {end_time.strftime('%H:%M')}</b><br>
                {block["task"]}<br>
                <span style="color:gray;font-size:12px;">
                Energy: {block["energy_fit"]}
                </span>
                </div>
                """,
                unsafe_allow_html=True
            )

            current_time = end_time

    st.divider()

    # ---------------- RISKS ----------------
    st.subheader("⚠️ Risk Flags")

    if data["risks"]:
        for r in data["risks"]:
            st.warning(r)
    else:
        st.success("No major risks detected.")

    # ---------------- NEXT ACTIONS ----------------
    st.subheader("✅ Start Now")

    for a in data["next_actions"]:
        st.checkbox(a, value=False)

