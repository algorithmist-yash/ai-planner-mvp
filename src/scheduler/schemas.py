from pydantic import BaseModel
from typing import List


class TimeBlock(BaseModel):
    task: str
    duration_minutes: int
    energy_fit: str


class DaySchedule(BaseModel):
    day: str
    blocks: List[TimeBlock]
    remaining_minutes: int
    overloaded: bool
