from datetime import date
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import E1
import E2
import A1
import A2
import A3

app = FastAPI(title="Student Attendance Tracker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

STATUSES = ["present", "absent"]


class AttendanceCreate(BaseModel):
    student_name: str
    roll_no: str
    attendance_date: date
    status: str


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


def check_token(token):
    email = A3.verify_token(token=token, token_type="access")
    if not email:
        raise HTTPException(status_code=401, detail="Invalid or Expired token")
    user_id = A3.get_user_id(email=email)
    if user_id is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user_id


def validate_attendance(student_name, roll_no, status):
    if student_name.strip() == "":
        raise HTTPException(status_code=422, detail="Student name cannot be empty")
    if roll_no.strip() == "":
        raise HTTPException(status_code=422, detail="Roll number cannot be empty")
    if status not in STATUSES:
        raise HTTPException(status_code=422, detail=f"Status must be one of {STATUSES}")


@app.get("/")
def hello():
    return {"message": "Student Attendance Tracker API. Docs at /docs"}


@app.post("/register")
def register(data: RegisterRequest):
    if data.username.strip() == "" or data.password.strip() == "":
        raise HTTPException(status_code=422, detail="Username and password cannot be empty")
    if data.email.count("@") != 1 or "." not in data.email.split("@")[1]:
        raise HTTPException(status_code=422, detail="Invalid email format")
    if A1.register_teacher(username=data.username, email=data.email, password=data.password):
        return {"message": "Teacher registered successfully"}
    raise HTTPException(status_code=409, detail="Email already registered")


@app.post("/login")
def login(data: LoginRequest):
    if data.email.strip() == "" or data.password.strip() == "":
        raise HTTPException(status_code=422, detail="Email and password cannot be empty")
    tokens = A2.verify_login(email=data.email, password=data.password)
    if not tokens:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return tokens


@app.post("/refresh")
def refresh(refresh_token = Header(None, convert_underscores=False)):
    access_token = A3.refresh_access_token(refresh_token=refresh_token)
    if not access_token:
        raise HTTPException(status_code=401, detail="Invalid or Expired refresh token")
    return {"access_token": access_token}


@app.get("/attendance")
def get_attendance(token = Header(None)):
    user_id = check_token(token)
    return E1.get_attendance(user_id=user_id)


@app.post("/attendance")
def mark_attendance(data: AttendanceCreate, token = Header(None)):
    user_id = check_token(token)
    validate_attendance(student_name=data.student_name, roll_no=data.roll_no, status=data.status)
    return E2.mark_attendance(user_id=user_id, student_name=data.student_name, roll_no=data.roll_no,
                              attendance_date=data.attendance_date, status=data.status)
