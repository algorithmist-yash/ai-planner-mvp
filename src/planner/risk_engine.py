from datetime import datetime
from typing import List
from src.core.schemas import NormalizedTask


def detect_risks(
    tasks: List[NormalizedTask],
    deadlines: List[str],
    overloaded: bool
) -> List[str]:

    risks = []

    if overloaded:
        risks.append("⚠️ Overload: Not all tasks fit in available time")

    for task, deadline in zip(tasks, deadlines):
        if task.ambiguity:
            risks.append(f"⚠️ Ambiguous task: '{task.original_text}'")

        if deadline:
            try:
                d = datetime.strptime(deadline, "%Y-%m-%d")
                days = (d - datetime.now()).days
                if days <= 2:
                    risks.append(f"⚠️ Tight deadline: '{task.original_text}'")
            except Exception:
                pass

    return risks
