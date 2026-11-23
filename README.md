# student-attendance-tracker

# Team - Student Attendance Tracker

| Partner 1 | Partner 2 | Partner 3 | Project |
|---|---|---|---|
| Aryan | Rehaan | Harsita | Student Attendance Tracker |

## 1. Who is doing what

| Day | Partner | What will you do? | Completed? | What are you going to work on next? | Stuck on? |
|---|---|---|---|---|---|
| Day 1 | Aryan | Built database.py (engine, tables, hasher, JWT config), requirements.txt and .gitignore | YES | The full main.py, A3 (refresh token) | No |
| Day 1 | Rehaan | Built E1 (get attendance) and E2 (mark attendance) | YES | create the Dockerfile, set up the frontend structure | No |
| Day 1 | Harsita | Set up GitHub repo, README and collaborators. | YES | Built A1 (register) and A2 (login) with JWT token helpers | No |
| Day 2 | Aryan | The full main.py, A3 (refresh token) | YES | Test all endpoints in /docs + Frontend | No |
| Day 2 | Rehaan | created the Dockerfile, set up the frontend structure | YES | Docker | No |
| Day 2 | Harsita | Built A1 (register) and A2 (login) with JWT token helpers | YES | Frontend | Nothing |
| Day 3 | Aryan | | | | |
| Day 3 | Rehaan | | | | |
| Day 3 | Harsita | | | | |

## 2. API contract (from Section 3 of the PRD)

Backend runs on **port 8001** with CORS enabled so the React frontend can communicate with it.

| # | What it does | Method | Path | Request body | Success code |
|---|---|---|---|---|---|
| A1 | Register a new teacher | POST | `/register` | `{ username, email, password }` | 200 |
| A2 | Login and generate JWT access and refresh tokens | POST | `/login` | `{ email, password }` | 200 |
| A3 | Generate a new access token using a refresh token | POST | `/refresh` | — (refresh token in `refresh_token` header) | 200 |
| E1 | Get all attendance records created by the logged-in teacher | GET | `/attendance` | — (access token in `token` header) | 200 |
| E2 | Mark a student's attendance and associate it with the logged-in teacher | POST | `/attendance` | `{ student_name, roll_no, attendance_date, status }` + access token in `token` header | 200 |

## 3. Rules the API checks (from Section 4 of the PRD)

| Rule | Status |
|---|---|
| Registering with an email that already exists | 409 |
| Logging in with incorrect email or password | 401 |
| Using an invalid or expired access token | 401 |
| Using an invalid or expired refresh token | 401 |
| Accessing attendance records without authentication | 401 |
| Sending missing or empty required fields | 422 |
| Registering with an invalid email format | 422 |
| Providing a status other than present or absent | 422 |

Every error returns a meaningful message.

## 4. Endpoint tracker

Status: ✅ done · 🟡 in progress · ⬜ not started

| # | Method + path | Built | Rules checked in /docs | Connected to React | Who |
|---|---|---|---|---|---|
| A1 | POST /register | ✅ | ✅ | ⬜ | Harsita + Aryan |
| A2 | POST /login | ✅ | ✅ | ⬜ | Harsita + Aryan |
| A3 | POST /refresh | ✅ | ✅ | ⬜ | Aryan |
| E1 | GET /attendance | ✅ | ⬜ | ⬜ | Rehaan + Aryan |
| E2 | POST /attendance | ✅ | ⬜ | ⬜ | Rehaan + Aryan |

## 5. Frontend tracker

| Part (from section 5 of your PRD) | Shows the data | Buttons work | Shows API errors | Who |
|---|---|---|---|---|
| Registration | ⬜ | ⬜ | ⬜ | |
| Login | ⬜ | ⬜ | ⬜ | |
| Attendance Dashboard | ⬜ | ⬜ | ⬜ | |
| Mark Attendance (Bonus) | ⬜ | ⬜ | ⬜ | |

Frontend requirements (PRD): real API calls only, no hardcoded data · JWT sent on protected endpoints · refresh-token handling when the access token expires · success/error messages shown · logout on the dashboard · empty-state message when there are no records.

## 6. Tech Stack & Deployment

- **Backend:** FastAPI, SQLite, SQLAlchemy, Pydantic, PyJWT, argon2-cffi
- **Frontend:** React, Vite
- **Deployment:** Docker, GitHub Actions CI/CD, AWS EC2
- **Database:** `attendance.db` (Persisted via Docker volume mount on EC2)

## 7. How to Run Locally

### Backend
1. Navigate to the `BACKEND` folder.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload --port 8001
   ```
4. Open Swagger UI: http://127.0.0.1:8001/docs

### Frontend
1. Navigate to the `FRONTEND` folder.
2. Install dependencies and start the dev server:
   ```bash
   npm install
   npm run dev
   ```

The backend API address is kept in one place in the frontend:
```js
const API_URL = "http://127.0.0.1:8001";
```