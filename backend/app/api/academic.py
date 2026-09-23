from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.academic import Mark, Attendance
from app.models.user import User
from app.schemas.academic import MarkCreate, MarkResponse, AttendanceCreate, AttendanceResponse
from app.api.deps import get_current_active_staff, get_current_user

router = APIRouter()

@router.post("/marks", response_model=MarkResponse)
def add_mark(
    mark_in: MarkCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_staff)
):
    if not current_user.staff_profile:
        raise HTTPException(status_code=400, detail="User is not a staff member")
        
    db_mark = Mark(
        **mark_in.model_dump(),
        staff_id=current_user.staff_profile.id
    )
    db.add(db_mark)
    db.commit()
    db.refresh(db_mark)
    return db_mark

@router.get("/marks/student/{student_id}", response_model=List[MarkResponse])
def get_student_marks(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # In a real app, verify that the user is allowed to see this student's marks
    marks = db.query(Mark).filter(Mark.student_id == student_id).all()
    return marks

@router.post("/attendance", response_model=AttendanceResponse)
def add_attendance(
    attendance_in: AttendanceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_staff)
):
    if not current_user.staff_profile:
        raise HTTPException(status_code=400, detail="User is not a staff member")
        
    db_att = Attendance(
        **attendance_in.model_dump(),
        staff_id=current_user.staff_profile.id
    )
    db.add(db_att)
    db.commit()
    db.refresh(db_att)
    return db_att
