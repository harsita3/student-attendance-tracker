from database import Attendance

def get_attendance(db, user_id):
    records = db.query(Attendance).filter(
        Attendance.user_id == user_id
    ).all()

    return records