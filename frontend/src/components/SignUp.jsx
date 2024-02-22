import { Link, useNavigate } from "react-router-dom";
import Auth from "./Auth";
import AuthButton from "./AuthButton";
import { useState } from "react";

export default function SignUp() {
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const history = useNavigate();
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("/users", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          firstname: firstname,
          lastname: lastname,
          email: email,
          password: password,
          "confirm-password": confirmPassword,
        }),
      });
      if (!response.ok) {
        throw new Error("Error while creating user");
      }

      const data = await response.json();
      setEmail("");
      setPassword("");
      setConfirmPassword("");
      console.log(data)

      history("/login");
    } catch (error) {
      console.error("Sign-up failed:", error.message);
      //setError("Check your details and try again.");
    }
  };

  return (
    <Auth>
      <div>
        <h3>Sign Up</h3>
        <div className="auth-header">
          <p>
            Already have an account? <Link to="/login">Sign in Here</Link>
          </p>
        </div>
        <div>
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <div className="row gx-1">
                <div className="col-sm-6">
                  <label className="form-label">First Name</label>
                  <input
                    type="text"
                    className="form-control"
                    id="firstname"
                    value={firstname}
                    onChange={(event) => setFirstname(event.target.value)}
                  />
                </div>
                <div className="col-sm-6">
                  <label className="form-label">Last Name</label>
                  <input
                    type="text"
                    className="form-control"
                    id="lastname"
                    value={lastname}
                    onChange={(event) => setLastname(event.target.value)}
                  />
                </div>
              </div>
            </div>
            <div className="mb-3">
              <label className="form-label">Email address</label>
              <input
                type="email"
                className="form-control"
                id="email"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Password</label>
              <input
                type="password"
                className="form-control"
                id="password"
                value={password}
                onChange={(event) => setPassword(event.target.value)}
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Confirm Password</label>
              <input
                type="password"
                className="form-control"
                id="confirm_password"
                value={confirmPassword}
                onChange={(event) => setConfirmPassword(event.target.value)}
              />
            </div>
            <AuthButton name="Sign up Here" />
          </form>
        </div>
      </div>
    </Auth>
  );
}
