from sqlalchemy import create_engine, String, Column, Integer, Float, Date, ForeignKey, func
from sqlalchemy.orm import Session, declarative_base
from datetime import datetime, timedelta, timezone
import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from database import engine, Session, User, ph, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRY, REFRESH_TOKEN_EXPIRY


ACCESS_TOKEN_EXPIRY = 15 #mins
REFRESH_TOKEN_EXPIRY = 7 * 24 * 60
SECRET_KEY = "SECRET123"
ALGORITHM = "HS256"

# A2: Login and generate JWT access and refresh tokens
def verify_login(email, password):
    session = Session(engine)
    user = session.query(User).filter_by(email=email).first()
    
    if user is None:
        session.close()
        return False
        
    try:
        ph.verify(user.hashed_password, password)
    except VerifyMismatchError:
        session.close()
        return False
        
    session.close()
    
    access_token = create_token(email=email, token_type="access")
    refresh_token = create_token(email=email, token_type="refresh")
    
    return {"access_token": access_token, "refresh_token": refresh_token}

def create_token(email, token_type):
    time = ACCESS_TOKEN_EXPIRY
    if token_type == "refresh":
        time = REFRESH_TOKEN_EXPIRY
        
    payload = {
        "email": email,
        "token_type": token_type,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=time)
    }
    token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token, token_type):
    try:
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
    except:
        return False

    if payload["token_type"] == token_type:
        return payload["email"]
    return False