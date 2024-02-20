import { Link } from "react-router-dom";
import Auth from "./Auth";
import AuthButton from "./AuthButton";

export default function SignIn() {
  return (
    <Auth>
      <div>
        <h3>Sign In</h3>
        <div classNameName="auth-header">
          <p>
            Don't have an Account yet? <Link to="/register">Sign up Here</Link>
          </p>
        </div>
        <div>
          <form>
            <div classNameName="mb-3">
              <label classNameName="form-label">Email address</label>
              <input type="email" classNameName="form-control" />
              <div id="emailHelp" classNameName="form-text">
                We'll never share your email with anyone else.
              </div>
            </div>
            <div classNameName="mb-3">
              <label classNameName="form-label">Password</label>
              <input type="password" classNameName="form-control" />
            </div>
            <AuthButton name="Sign In" />
          </form>
        </div>
      </div>
    </Auth>
  );
}
