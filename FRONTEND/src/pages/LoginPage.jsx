import { useState } from 'react';
import { useNavigate } from 'react-router';
import { API_URL } from '../config.js';


function LoginPage() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const navigate = useNavigate();

    async function handleLogin(event) {
        event.preventDefault();

        try {
            const res = await fetch(`${API_URL}/login`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email: email, password: password }),
            });
            const data = await res.json();

            if (!res.ok) {
                setMessage(data.detail);
                return;
            }

            localStorage.setItem("access_token", data.access_token);
            localStorage.setItem("refresh_token", data.refresh_token);
            navigate("/dashboard");
        } catch {
            setMessage("Could not connect to the server");
        }
    }

    return (
        <>
        <h2>Teacher Login</h2>
        <form onSubmit={handleLogin}>
            <p>
                <label>Email: </label>
                <input value={email} onChange={(e) => setEmail(e.target.value)} />
            </p>
            <p>
                <label>Password: </label>
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            </p>
            <button type="submit">Login</button>
        </form>
        <p>{message}</p>
        </>
    );
}

export default LoginPage;
