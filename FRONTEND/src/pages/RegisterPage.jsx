import { useState } from 'react';
import { useNavigate } from 'react-router';
import { API_URL } from '../config.js';


function RegisterPage() {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const navigate = useNavigate();

    async function handleRegister(event) {
        event.preventDefault();

        try {
            const res = await fetch(`${API_URL}/register`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username: username, email: email, password: password }),
            });
            const data = await res.json();

            if (!res.ok) {
                setMessage(data.detail);
                return;
            }

            setMessage(data.message);
            navigate("/login");
        } catch {
            setMessage("Could not connect to the server");
        }
    }

    return (
        <>
        <h2>Teacher Registration</h2>
        <form onSubmit={handleRegister}>
            <p>
                <label>Username: </label>
                <input value={username} onChange={(e) => setUsername(e.target.value)} />
            </p>
            <p>
                <label>Email: </label>
                <input value={email} onChange={(e) => setEmail(e.target.value)} />
            </p>
            <p>
                <label>Password: </label>
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            </p>
            <button type="submit">Register</button>
        </form>
        <p>{message}</p>
        </>
    );
}

export default RegisterPage;