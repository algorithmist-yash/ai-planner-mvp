def ensure_non_empty_tasks(tasks):
    if not tasks:
        raise ValueError("No tasks provided")


def ensure_time_reasonable(minutes: int):
    if minutes <= 0 or minutes > 600:
        raise ValueError("Unreasonable task duration")
