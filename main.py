from src.core.task_parser import parse_tasks
from src.core.schemas import RawTask
from src.planner.priority_engine import compute_priority

if __name__ == "__main__":
    raw = [
        RawTask(text="Study AI"),
        RawTask(text="Submit AI assignment", deadline="2026-01-22")
    ]

    parsed = parse_tasks(raw)

    for t, r in zip(parsed, raw):
        priority_info = compute_priority(t, r.deadline)
        print(f"\nTask: {t.original_text}")
        print(priority_info)

