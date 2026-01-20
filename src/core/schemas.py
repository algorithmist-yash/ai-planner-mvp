from typing import List, Optional
from pydantic import BaseModel


class RawTask(BaseModel):
    text: str
    deadline: Optional[str] = None


class SubTask(BaseModel):
    title: str
    estimated_minutes: int
    dependency: Optional[str] = None


class NormalizedTask(BaseModel):
    original_text: str
    subtasks: List[SubTask]
    ambiguity: bool
