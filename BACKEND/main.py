from datetime import date
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import E1
import E2
import e3
import A1
import A2

app = FastAPI(title="Student Attendance Tracker")

STATUSES = ["present", "absent"]


# ---------- Request bodies (Pydantic) ----------
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
    email = e3.verify_token(token=token, token_type="access")
    if not email:
        raise HTTPException(status_code=401, detail="Invalid or Expired token")
    user_id = e3.get_user_id(email=email)
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


# ---------- A1: Register ----------
@app.post("/register", status_code=201)
def register(data: RegisterRequest):
    if data.username.strip() == "" or data.password.strip() == "":
        raise HTTPException(status_code=422, detail="Username and password cannot be empty")
    if "@" not in data.email or "." not in data.email:
        raise HTTPException(status_code=422, detail="Invalid email format")
    if A1.register_teacher(username=data.username, email=data.email, password=data.password):
        return {"message": "Teacher registered successfully"}
    raise HTTPException(status_code=409, detail="Email already registered")


# ---------- A2: Login ----------
@app.post("/login")
def login(data: LoginRequest):
    tokens = A2.verify_login(email=data.email, password=data.password)
    if not tokens:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return tokens


# ---------- A3: Refresh ----------
@app.post("/refresh")
def refresh(refresh_token = Header(None, convert_underscores=False)):
    access_token = e3.refresh_access_token(refresh_token=refresh_token)
    if not access_token:
        raise HTTPException(status_code=401, detail="Invalid or Expired refresh token")
    return {"access_token": access_token}


# ---------- E1: Get attendance ----------
@app.get("/attendance")
def get_attendance(token = Header(None)):
    user_id = check_token(token)
    return E1.get_attendance(user_id=user_id)


# ---------- E2: Mark attendance ----------
@app.post("/attendance", status_code=201)
def mark_attendance(data: AttendanceCreate, token = Header(None)):
    user_id = check_token(token)
    validate_attendance(student_name=data.student_name, roll_no=data.roll_no, status=data.status)
    return E2.mark_attendance(user_id=user_id, student_name=data.student_name, roll_no=data.roll_no,
                              attendance_date=data.attendance_date, status=data.status)
