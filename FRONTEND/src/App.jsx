import { Routes, Route } from "react-router"
import LoginPage from './pages/LoginPage.jsx'

function App() {

  return (
    <>
    <Routes>
      <Route path="/" element={<LoginPage/>} />
      <Route path="/login" element={<LoginPage/>} />
      <Route path="*" element={<h1>404 Not Found</h1>} />
    </Routes>
    </>
  )
}

export default App
