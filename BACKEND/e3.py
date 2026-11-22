from fastapi import FastAPI, HTTPException, Header
from datetime import datetime, timedelta, timezone
import jwt

app = FastAPI(title="Student Attendance Tracker")

ACCESS_TOKEN_EXPIRY = 15 #mins
REFRESH_TOKEN_EXPIRY = 7 * 24 * 60
SECRET_KEY = "SECRET123"
ALGORITHM = "HS256"


# ---------- Tokens ----------

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


# ---------- A3: Generate a new access token using a refresh token ----------

@app.post("/refresh")
def refresh(refresh_token = Header(None, convert_underscores=False)):
    email = verify_token(token=refresh_token, token_type="refresh")
    if not email:
        raise HTTPException(status_code=401, detail="Invalid or Expired refresh token")

    access_token = create_token(email=email, token_type="access")
    return {"access_token": access_token}
