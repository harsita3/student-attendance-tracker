# student-attendance-tracker

# Team - Student Attendance Tracker

| Partner 1 | Partner 2 | Partner 3 | Project |
|---|---|---|---|
| Aryan | Rehaan | Harsita | Student Attendance Tracker |

## 1. Who is doing what

Update your own row at every check-in.

| Day | Partner | What will you do? | Completed? | What are you going to work on next? | Stuck on? |
|---|---|---|---|---|---|
| Day 1 | Aryan | Built database.py (engine, tables, hasher, JWT config), requirements.txt and .gitignore | YES | The full main.py, A3 (refresh token) | No |
| Day 1 | Rehaan | Built E1 (get attendance) and E2 (mark attendance) | YES | create the Dockerfile, set up the frontend structure | No |
| Day 1 | Harsita | Set up GitHub repo, README and collaborators. | YES | Built A1 (register) and A2 (login) with JWT token helpers | No |
| Day 2 | Aryan | The full main.py, A3 (refresh token) | YES | Test all endpoints in /docs + Frontend | No |
| Day 2 | Rehaan | created the Dockerfile, set up the frontend structure | Yes | Docker | No |
| Day 2 | Harsita | Built A1 (register) and A2 (login) with JWT token helpers | Yes | Frontend | Nothing |
| Day 3 | Aryan | | | | |
| Day 3 | Rehaan | | | | |
| Day 3 | Harsita | | | | |

## 2. Endpoint tracker

Status: ✅ done · 🟡 in progress · ⬜ not started

| # | Method + path | Built | Rules checked in /docs | Connected to React | Who |
|---|---|---|---|---|---|
| A1 | POST /register | ✅ | ⬜ | ⬜ | Harsita + Aryan |
| A2 | POST /login | ✅| ⬜ | ⬜ | Harsita + Aryan |
| A3 | POST /refresh | ✅ | ⬜ | ⬜ | Aryan |
| E1 | GET /attendance | ✅ | ⬜ | ⬜ | Rehaan + Aryan |
| E2 | POST /attendance | ✅ | ⬜ | ⬜ | Rehaan + Aryan |

## 3. Frontend tracker

| Part (from section 5 of your PRD) | Shows the data | Buttons work | Shows API errors | Who |
|---|---|---|---|---|
| Registration | ⬜ | ⬜ | ⬜ | |
| Login | ⬜ | ⬜ | ⬜ |  |
| Attendance Dashboard | ⬜ | ⬜ | ⬜ |  |
| Mark Attendance (Bonus) | ⬜ | ⬜ | ⬜ |  |

## 4. Tech Stack & Deployment

- **Backend:** FastAPI, SQLite, SQLAlchemy, Pydantic, PyJWT, argon2-cffi
- **Frontend:** React, Vite
- **Deployment:** Docker, GitHub Actions CI/CD, AWS EC2
- **Database:** `attendance.db` (Persisted via Docker volume mount on EC2)

## 5. How to Run Locally

### Backend
1. Navigate to the `backend` folder.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
