def format_output(
    task_breakdown,
    priority_table,
    schedule,
    risks,
    next_actions
):
    print("\n### 1️⃣ Task Breakdown")
    for t in task_breakdown:
        print(f"- {t}")

    print("\n### 2️⃣ Priority Table")
    print("| Task | Priority | Deadline | Reason |")
    for row in priority_table:
        print(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")

    print("\n### 3️⃣ Schedule Plan")
    print(f"📅 {schedule.day}")
    for b in schedule.blocks:
        print(f"• {b.task} | {b.duration_minutes} min | {b.energy_fit}")

    print("\n### 4️⃣ Risk Flags")
    for r in risks:
        print(r)

    print("\n### 5️⃣ Next Actions")
    for a in next_actions:
        print(f"✅ {a}")
