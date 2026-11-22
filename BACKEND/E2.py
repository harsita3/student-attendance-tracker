from database import Attendance

def mark_attendance(db, user_id, attendance):
    new_record = Attendance(
        user_id=user_id,
        student_name=attendance.student_name,
        roll_no=attendance.roll_no,
        attendance_date=attendance.attendance_date,
        status=attendance.status
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return new_record