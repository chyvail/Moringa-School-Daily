import { Link, useNavigate } from "react-router-dom";
import Auth from "./Auth";
import AuthButton from "./AuthButton";
import React, { useState } from "react";


export default function SignIn() {
  // state
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  const history = useNavigate();
  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email: email,
          password: password,
        }),
      });

      if (!response.ok) {
        throw new Error("Error while validating user");
      }

      const data = await response.json();
      setEmail("");
      setPassword("");
      console.log(data)
      const access = data['jwt-access-token'];
      localStorage.setItem("accessToken", access);

      // Redirect to home
      history("/");

    } catch (error) {
      console.error("Login failed:", error.message);
      setError("Check your username and password and try again.");
    }
  };
  return (
    <Auth>
      <div>
        <h3>Sign In</h3>
        <div className="auth-header">
          <p>
            Don't have an Account yet? <Link to="/register">Sign up Here</Link>
          </p>
        </div>
        <div>
          <form onSubmit={handleLogin}>
            <div className="mb-3">
              <label className="form-label">Email address</label>
              <input
                id="email"
                type="email"
                className="form-control"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
              />
              <div id="emailHelp" className="form-text">
                We'll never share your email with anyone else.
              </div>
            </div>
            <div className="mb-3">
              <label className="form-label">Password</label>
              <input
                id="password"
                type="password"
                className="form-control"
                value={password}
                onChange={(event) => setPassword(event.target.value)}
              />
            </div>
            <AuthButton name="Sign In" />
            {error && <div className="alert alert-danger">{error}</div>}
          </form>
        </div>
      </div>
    </Auth>
  );
}
