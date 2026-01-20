from typing import List
from src.scheduler.schemas import DaySchedule, TimeBlock


BUFFER_RATIO = 0.15


def schedule_day(
    day: str,
    available_minutes: int,
    tasks: List[dict]
) -> DaySchedule:

    used = 0
    blocks = []
    overloaded = False

    for task in tasks:
        task_time = int(task["estimated_minutes"] * (1 + BUFFER_RATIO))

        if used + task_time <= available_minutes:
            blocks.append(
                TimeBlock(
                    task=task["title"],
                    duration_minutes=task_time,
                    energy_fit=task["energy"]
                )
            )
            used += task_time
        else:
            overloaded = True
            break

    # ✅ ADD HERE (RIGHT BEFORE RETURN)
    if overloaded:
        print("⚠️ WARNING: Schedule overloaded. Some tasks not scheduled.")

    return DaySchedule(
        day=day,
        blocks=blocks,
        remaining_minutes=max(0, available_minutes - used),
        overloaded=overloaded
    )

