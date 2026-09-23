import enum
from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class RoleEnum(str, enum.Enum):
    ADMIN = "ADMIN"
    HOD = "HOD"
    STAFF = "STAFF"
    STUDENT = "STUDENT"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    is_active = Column(Boolean, default=True)
    profile_photo_url = Column(String, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    student_profile = relationship("Student", back_populates="user", uselist=False)
    staff_profile = relationship("Staff", back_populates="user", uselist=False)

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    code = Column(String, unique=True, nullable=False)
    
    # Relationships
    students = relationship("Student", back_populates="department")
    staff = relationship("Staff", back_populates="department")

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    register_number = Column(String, unique=True, index=True, nullable=False)
    year = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="student_profile")
    department = relationship("Department", back_populates="students")

class Staff(Base):
    __tablename__ = "staff"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    employee_id = Column(String, unique=True, index=True, nullable=False)
    designation = Column(String, nullable=False)
    is_hod = Column(Boolean, default=False)
    
    # Relationships
    user = relationship("User", back_populates="staff_profile")
    department = relationship("Department", back_populates="staff")
