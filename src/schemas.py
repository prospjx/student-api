from pydantic import BaseModel
from typing import List, Optional

class StudentPreferences(BaseModel):
    max_credits_per_term: int = 18
    preferred_days_off: List[str] = []
    difficulty_tolerance: str = "medium"  # low, medium, high
    preferred_time_of_day: str = "any"    # morning, afternoon, evening, any

class StudentProfile(BaseModel):
    student_id: str
    name: str
    preferences: StudentPreferences

    class Config:
        from_attributes = True
