from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class MarkBase(BaseModel):
    subject_id: int
    exam_type: str
    score: float
    max_score: float

class MarkCreate(MarkBase):
    student_id: int

class MarkResponse(MarkBase):
    id: int
    student_id: int
    staff_id: int
    
    class Config:
        from_attributes = True

class AttendanceBase(BaseModel):
    subject_id: int
    date: date
    is_present: bool

class AttendanceCreate(AttendanceBase):
    student_id: int

class AttendanceResponse(AttendanceBase):
    id: int
    student_id: int
    staff_id: int
    
    class Config:
        from_attributes = True
