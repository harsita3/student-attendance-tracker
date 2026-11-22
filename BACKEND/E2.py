from sqlalchemy.orm import Session
from database import engine, Attendance

def mark_attendance(user_id, student_name, roll_no, attendance_date, status):
    session = Session(engine)

    new_attendance = Attendance(
        user_id=user_id,
        student_name=student_name,
        roll_no=roll_no,
        attendance_date=attendance_date,
        status=status
    )

    session.add(new_attendance)
    session.commit()

    response = {
        "id": new_attendance.id,
        "user_id": new_attendance.user_id,
        "student_name": new_attendance.student_name,
        "roll_no": new_attendance.roll_no,
        "attendance_date": new_attendance.attendance_date,
        "status": new_attendance.status
    }

    session.close()
    return response