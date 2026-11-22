from sqlalchemy.orm import Session
from argon2 import PasswordHasher
from database import engine, User

ph = PasswordHasher()


# A1: Register a new teacher

def register_teacher(username, email, password):
    session = Session(engine)
    user_exists = session.query(User).filter_by(email=email).first()

    if user_exists is not None:
        session.close()
        return False

    session.add(User(username=username, email=email, hashed_password=ph.hash(password)))
    session.commit()
    session.close()
    return True
