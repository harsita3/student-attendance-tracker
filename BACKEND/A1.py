from sqlalchemy import create_engine, String, Column, Integer, Float, Date, ForeignKey, func
from sqlalchemy.orm import Session, declarative_base
from datetime import datetime, timedelta, timezone
import jwt
from database import engine, Session, User, ph


ACCESS_TOKEN_EXPIRY = 15 #mins
REFRESH_TOKEN_EXPIRY = 7 * 24 * 60
SECRET_KEY = "SECRET123"
ALGORITHM = "HS256"


# A1: Register a new teacher
def register_teacher(username, email, password):
    session = Session(engine)
    user_exists = session.query(User).filter_by(email=email).first()

    if user_exists is not None:
        session.close()
        return False

    session.add(User(
        username=username,
        email=email,
        hashed_password=ph.hash(password)
    ))
    session.commit()
    session.close()
    return True