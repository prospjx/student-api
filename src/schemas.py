from pydantic import BaseModel
from typing import List, Optional

class StudentPreferences(BaseModel):
    max_credits_per_term: int = 18
    preferred_days_off: List[str] = []
    difficulty_tolerance: str = "medium"  # low, medium, high
    preferred_time_of_day: str = "any"    # morning, afternoon, evening, any
    
    # Life planning preferences
    wake_up_time: str = "07:00"           # e.g., "07:00"
    sleep_time: str = "23:00"             # e.g., "23:00"
    study_hours_per_day: int = 3          # target study hours per day
    transit_time_minutes: int = 45        # transit time one-way to/from campus
    gym_time_preference: str = "afternoon" # morning, afternoon, evening, none
    gym_duration_minutes: int = 60        # workout duration in minutes

class StudentProfile(BaseModel):
    student_id: str
    name: str
    preferences: StudentPreferences

    class Config:
        from_attributes = True
