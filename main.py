from src.core.task_parser import parse_tasks
from src.core.schemas import RawTask
from src.planner.priority_engine import compute_priority
from src.planner.risk_engine import detect_risks
from src.scheduler.schedule_builder import schedule_day
from src.utils.output_formatter import format_output

if __name__ == "__main__":
    raw_tasks = [
        RawTask(text="Study AI"),
        RawTask(text="Submit AI assignment", deadline="2026-01-22"),
        RawTask(text="Prepare exam", deadline="2026-01-20")
    ]

    parsed = parse_tasks(raw_tasks)

    enriched = []
    priority_table = []

    for task, raw in zip(parsed, raw_tasks):
        p = compute_priority(task, raw.deadline)
        total_minutes = sum(st.estimated_minutes for st in task.subtasks)

        enriched.append({
            "title": task.original_text,
            "estimated_minutes": total_minutes,
            "energy": "High" if p["priority"] == "P1" else "Medium",
            "priority": p["priority"]
        })

        priority_table.append([
            task.original_text,
            p["priority"],
            raw.deadline or "—",
            ", ".join(p["reasons"])
        ])

    priority_order = {"P1": 1, "P2": 2, "P3": 3}
    enriched.sort(key=lambda x: priority_order[x["priority"]])

    schedule = schedule_day(
        day="Today",
        available_minutes=180,
        tasks=enriched
    )

    risks = detect_risks(
        parsed,
        [r.deadline for r in raw_tasks],
        schedule.overloaded
    )

    format_output(
        task_breakdown=[t.original_text for t in parsed],
        priority_table=priority_table,
        schedule=schedule,
        risks=risks,
        next_actions=[b.task for b in schedule.blocks]
    )

