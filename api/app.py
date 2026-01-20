from fastapi import FastAPI
from api.schemas import PlanRequest, PlanResponse
from src.core.task_parser import parse_tasks
from src.core.schemas import RawTask
from src.planner.priority_engine import compute_priority
from src.planner.risk_engine import detect_risks
from src.scheduler.schedule_builder import schedule_day

app = FastAPI(title="AI Planning Assistant MVP")


@app.post("/plan", response_model=PlanResponse)
def generate_plan(request: PlanRequest):

    raw_tasks = [
        RawTask(text=t.text, deadline=t.deadline)
        for t in request.tasks
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
        day=request.day,
        available_minutes=request.available_minutes,
        tasks=enriched
    )

    risks = detect_risks(
        parsed,
        [t.deadline for t in raw_tasks],
        schedule.overloaded
    )

    return {
        "task_breakdown": [t.original_text for t in parsed],
        "priority_table": priority_table,
        "schedule": schedule.dict(),
        "risks": risks,
        "next_actions": [b.task for b in schedule.blocks]
    }
