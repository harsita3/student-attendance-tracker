import os
from sqlalchemy import create_engine, String, Column, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime

DB_URL = os.getenv("DB_URL", "sqlite:///attendance.db")
engine = create_engine(DB_URL)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    student_name = Column(String, nullable=False)
    roll_no = Column(String, nullable=False)
    attendance_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)


Base.metadata.create_all(engine)
