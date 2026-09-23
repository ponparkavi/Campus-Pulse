import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.core.database import SessionLocal
from app.models.user import User, RoleEnum, Department, Student
from app.core.security import get_password_hash

def seed_db():
    db = SessionLocal()
    
    # Create department
    cs_dept = db.query(Department).filter(Department.code == "CS").first()
    if not cs_dept:
        cs_dept = Department(name="Computer Science", code="CS")
        db.add(cs_dept)
        db.commit()
        db.refresh(cs_dept)

    # Create Admin
    admin = db.query(User).filter(User.email == "admin@campuspulse.edu").first()
    if not admin:
        admin = User(
            email="admin@campuspulse.edu",
            hashed_password=get_password_hash("admin123"),
            full_name="System Admin",
            role=RoleEnum.ADMIN
        )
        db.add(admin)
        db.commit()

    # Create Student
    student_user = db.query(User).filter(User.email == "student@campuspulse.edu").first()
    if not student_user:
        student_user = User(
            email="student@campuspulse.edu",
            hashed_password=get_password_hash("student123"),
            full_name="John Doe",
            role=RoleEnum.STUDENT
        )
        db.add(student_user)
        db.commit()
        db.refresh(student_user)
        
        student_profile = Student(
            user_id=student_user.id,
            department_id=cs_dept.id,
            register_number="CS2026001",
            year=1,
            semester=1
        )
        db.add(student_profile)
        db.commit()

    print("Database seeded with admin@campuspulse.edu (admin123) and student@campuspulse.edu (student123)")
    db.close()

if __name__ == "__main__":
    seed_db()
