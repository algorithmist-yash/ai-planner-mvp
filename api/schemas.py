from typing import List, Optional
from pydantic import BaseModel


class TaskInput(BaseModel):
    text: str
    deadline: Optional[str] = None


class PlanRequest(BaseModel):
    tasks: List[TaskInput]
    available_minutes: int
    day: str


class PlanResponse(BaseModel):
    task_breakdown: List[str]
    priority_table: List[List[str]]
    schedule: dict
    risks: List[str]
    next_actions: List[str]
