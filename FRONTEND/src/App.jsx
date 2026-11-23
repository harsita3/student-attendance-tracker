import { Routes, Route, Link } from "react-router"
import RegisterPage from './pages/RegisterPage.jsx'
import LoginPage from './pages/LoginPage.jsx'
import DashboardPage from './pages/DashboardPage.jsx'

function App() {

  return (
    <>
    <nav>
      <Link to="/register">Register</Link> | <Link to="/login">Login</Link> | <Link to="/dashboard">Dashboard</Link>
    </nav>
    <Routes>
      <Route path="/" element={<LoginPage/>} />
      <Route path="/register" element={<RegisterPage/>} />
      <Route path="/login" element={<LoginPage/>} />
      <Route path="/dashboard" element={<DashboardPage/>} />
      <Route path="*" element={<h1>404 Not Found</h1>} />
    </Routes>
    </>
  )
}

export default App
