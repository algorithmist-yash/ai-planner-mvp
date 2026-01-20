from src.core.task_parser import parse_tasks
from src.core.schemas import RawTask

if __name__ == "__main__":
    raw = [
        RawTask(text="Study AI"),
        RawTask(text="Finish assignment")
    ]

    parsed = parse_tasks(raw)

    for t in parsed:
        print(t)
