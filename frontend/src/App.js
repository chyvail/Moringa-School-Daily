import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SignIn from "./components/SignIn";
import Home from "./pages/Home";
import SignUp from "./components/SignUp";
import Footer from "./components/Footer";
import { SchoolContext } from "./contexts/SchoolContext";
import { useState, useEffect } from "react";

function App() {
  // states
  const [user, setUser] = useState("");
  const [userEmail, setUserEmail] = useState("");
  const [userRole, setUserRole] = useState("");
  const [userId, setUserId] = useState("");

  // session token
  let accessToken = localStorage.getItem("accessToken");

  useEffect(() => {
    if (accessToken) {
      fetch("/user-token", {
        headers: { Authorization: `Bearer ${accessToken}` },
      })
        .then((res) => res.json())
        .then((data) => {
          setUser(data.firstname);
          setUserEmail(data.email);
          setUserRole(data.role);
          setUserId(data.id);
        });
    } else {
      setUser("");
    }
  }, [accessToken, setUser, userId, userRole, userEmail]);

  return (
    <SchoolContext.Provider
      value={{ user, setUser, userEmail, userRole, accessToken, userId }}
    >
      <BrowserRouter>
        <Routes>
          <Route path="/" element={accessToken ? <Home /> : <SignIn />} />
          <Route path="/home" element={<Home />} />
          <Route path="/login" element={<SignIn />} />
          <Route path="/register" element={<SignUp />} />
        </Routes>
        <Footer />
      </BrowserRouter>
    </SchoolContext.Provider>
  );
}

export default App;
