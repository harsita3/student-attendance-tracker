from sqlalchemy.orm import Session
from database import engine, Attendance

def get_attendance(user_id):
    session = Session(engine)

    records = session.query(Attendance).filter_by(user_id=user_id).all()

    response = []

    for record in records:
        response.append({
            "id": record.id,
            "student_name": record.student_name,
            "roll_no": record.roll_no,
            "attendance_date": record.attendance_date,
            "status": record.status,
            "created_at": record.created_at
        })

    session.close()
    return response