from typing import List
from src.core.schemas import RawTask, NormalizedTask, SubTask


AMBIGUOUS_KEYWORDS = [
    "study", "learn", "prepare", "work on", "improve", "revise"
]


def is_ambiguous(text: str) -> bool:
    text_lower = text.lower()
    return any(k in text_lower for k in AMBIGUOUS_KEYWORDS)


def naive_decompose(task_text: str) -> List[SubTask]:
    """
    Conservative default decomposition.
    Never assumes hidden steps.
    """
    return [
        SubTask(
            title=task_text,
            estimated_minutes=60  # safe default
        )
    ]


def parse_tasks(raw_tasks: List[RawTask]) -> List[NormalizedTask]:
    normalized = []

    for task in raw_tasks:
        ambiguous = is_ambiguous(task.text)
        subtasks = naive_decompose(task.text)

        normalized.append(
            NormalizedTask(
                original_text=task.text,
                subtasks=subtasks,
                ambiguity=ambiguous
            )
        )

    return normalized
