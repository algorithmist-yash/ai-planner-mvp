from datetime import datetime
from typing import Optional
from src.core.schemas import NormalizedTask


URGENT_KEYWORDS = ["exam", "submit", "submission", "deadline"]


def days_until(deadline: Optional[str]) -> Optional[int]:
    if not deadline:
        return None
    try:
        d = datetime.strptime(deadline, "%Y-%m-%d")
        return (d - datetime.now()).days
    except Exception:
        return None


def compute_priority(task: NormalizedTask, deadline: Optional[str]) -> dict:
    score = 0
    reasons = []

    if deadline:
        score += 3
        reasons.append("Has deadline")

        days = days_until(deadline)
        if days is not None and days <= 3:
            score += 5
            reasons.append("Deadline within 3 days")

    if task.ambiguity:
        score -= 2
        reasons.append("Task is ambiguous")

    total_minutes = sum(st.estimated_minutes for st in task.subtasks)
    if total_minutes > 120:
        score -= 1
        reasons.append("Long task")

    text = task.original_text.lower()
    if any(k in text for k in URGENT_KEYWORDS):
        score += 3
        reasons.append("Urgent keyword detected")

    if score >= 6:
        level = "P1"
    elif score >= 3:
        level = "P2"
    else:
        level = "P3"

    return {
        "priority": level,
        "score": score,
        "reasons": reasons
    }
