from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, Float
from sqlalchemy.orm import relationship
from app.core.database import Base

class Subject(Base):
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    semester = Column(Integer, nullable=False)
    credits = Column(Integer, default=3)
    
    department = relationship("Department")

class Class(Base):
    __tablename__ = "classes"
    
    id = Column(Integer, primary_key=True, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    year = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)
    section = Column(String, nullable=False)
    
    department = relationship("Department")

class StudentSubject(Base):
    __tablename__ = "student_subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))

class FacultySubject(Base):
    __tablename__ = "faculty_subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(Integer, ForeignKey("staff.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))

class Attendance(Base):
    __tablename__ = "attendance"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    staff_id = Column(Integer, ForeignKey("staff.id"))
    date = Column(Date, nullable=False)
    is_present = Column(Boolean, default=True)

class Mark(Base):
    __tablename__ = "marks"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    staff_id = Column(Integer, ForeignKey("staff.id"))
    exam_type = Column(String, nullable=False) # e.g. "MIDTERM", "FINAL", "INTERNAL"
    score = Column(Float, nullable=False)
    max_score = Column(Float, nullable=False)
