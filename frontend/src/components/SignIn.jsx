import { Link } from "react-router-dom";
import Auth from "./Auth";
import AuthButton from "./AuthButton";

export default function SignIn() {
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
          <form>
            <div className="mb-3">
              <label className="form-label">Email address</label>
              <input type="email" className="form-control" />
              <div id="emailHelp" className="form-text">
                We'll never share your email with anyone else.
              </div>
            </div>
            <div className="mb-3">
              <label className="form-label">Password</label>
              <input type="password" className="form-control" />
            </div>
            <AuthButton name="Sign In" />
          </form>
        </div>
      </div>
    </Auth>
  );
}
