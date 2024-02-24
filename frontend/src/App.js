import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SignIn from "./components/SignIn";
import Home from "./pages/Home";
import SignUp from "./components/SignUp";
import { SchoolContext } from "./contexts/SchoolContext";
import { useState, useEffect } from "react";
import SinglePost from "./pages/SinglePost";

function App() {
  // states
  const [user, setUser] = useState("");
  const [userEmail, setUserEmail] = useState("");
  const [userRole, setUserRole] = useState("");
  const [userId, setUserId] = useState("");
  const [postData, setPostData] = useState([]);

  // session token
  let accessToken = localStorage.getItem("accessToken");

  useEffect(() => {
    if (accessToken) {
      fetch("/user-token", {
        headers: { Authorization: `Bearer ${accessToken}` },
      })
        .then((res) => res.json())
        .then((data) => {
          setUser(`${data.firstname} ${data.lastname}`);
          setUserEmail(data.email);
          setUserRole(data.role);
          setUserId(data.id);
        });
    } else {
      setUser("");
    }
  }, [accessToken, setUser, userId, userRole, userEmail]);

  // get posts

  useEffect(() => {
    fetch("/contents")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        return response.json();
      })
      .then((data) => {
        setPostData(data);
      });
  }, []);

  return (
    <SchoolContext.Provider
      value={{
        user,
        setUser,
        userEmail,
        userRole,
        accessToken,
        userId,
        postData,
        setPostData
      }}
    >
      <BrowserRouter>
        <Routes>
          <Route path="/" element={accessToken ? <Home /> : <SignIn />} />
          <Route path="/home" element={<Home />} />
          <Route path="/login" element={<SignIn />} />
          <Route path="/register" element={<SignUp />} />
          <Route path="/posts/:id" element={<SinglePost />} />
        </Routes>
      </BrowserRouter>
    </SchoolContext.Provider>
  );
}

export default App;
