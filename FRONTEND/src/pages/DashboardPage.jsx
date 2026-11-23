import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router';
import { API_URL } from '../config.js';


function DashboardPage() {
    const [records, setRecords] = useState([]);
    const [message, setMessage] = useState("");
    const navigate = useNavigate();

    function logout() {
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
        navigate("/login");
    }

    useEffect(() => {
        async function getAttendance() {
            const res = await fetch(`${API_URL}/attendance`, {
                headers: { token: localStorage.getItem("access_token") },
            });
            return res;
        }

        async function refreshToken() {
            const res = await fetch(`${API_URL}/refresh`, {
                method: "POST",
                headers: { refresh_token: localStorage.getItem("refresh_token") },
            });
            if (!res.ok) return false;

            const data = await res.json();
            localStorage.setItem("access_token", data.access_token);
            return true;
        }

        async function loadAttendance() {
            try {
                let res = await getAttendance();

                if (res.status === 401) {
                    const refreshed = await refreshToken();
                    if (!refreshed) {
                        localStorage.removeItem("access_token");
                        localStorage.removeItem("refresh_token");
                        navigate("/login");
                        return;
                    }
                    res = await getAttendance();
                }

                const data = await res.json();

                if (!res.ok) {
                    setMessage(data.detail);
                    return;
                }

                setRecords(data);
                if (data.length === 0) {
                    setMessage("No attendance records found");
                }
            } catch {
                setMessage("Could not connect to the server");
            }
        }
        loadAttendance();
    }, [navigate]);

    return (
        <>
        <h2>My Attendance Records</h2>
        <p>Showing only your own attendance records.</p>
        <button onClick={logout}>Logout</button>
        <p>{message}</p>
        <table border="1">
            <thead>
                <tr>
                    <th>Student Name</th>
                    <th>Roll No</th>
                    <th>Date</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {records.map((record) => (
                    <tr key={record.id}>
                        <td>{record.student_name}</td>
                        <td>{record.roll_no}</td>
                        <td>{record.attendance_date}</td>
                        <td>{record.status}</td>
                    </tr>
                ))}
            </tbody>
        </table>
        </>
    );
}

export default DashboardPage;
