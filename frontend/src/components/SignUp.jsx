import { Link } from "react-router-dom";
import Auth from "./Auth";
import AuthButton from "./AuthButton";

export default function SignUp() {
  return (
    <Auth>
      <div>
        <h3>Sign Up</h3>
        <div classNameName="auth-header">
          <p>
            Already have an account? <Link to="/login">Sign in Here</Link>
          </p>
        </div>
        <div>
          <form>
            <div classNameName="mb-3">
              <div classNameName="row gx-1">
                <div classNameName="col-sm-6">
                  <label classNameName="form-label">First Name</label>
                  <input type="text" classNameName="form-control" />
                </div>
                <div classNameName="col-sm-6">
                  <label classNameName="form-label">Last Name</label>
                  <input type="text" classNameName="form-control" />
                </div>
              </div>
            </div>
            <div classNameName="mb-3">
              <label classNameName="form-label">Email address</label>
              <input type="email" classNameName="form-control" />
            </div>
            <div classNameName="mb-3">
              <label classNameName="form-label">Password</label>
              <input type="password" classNameName="form-control" />
            </div>
            <div classNameName="mb-3">
              <label classNameName="form-label">Confirm Password</label>
              <input type="password" classNameName="form-control" />
            </div>
            <AuthButton name="Sign up Here" />
          </form>
        </div>
      </div>
    </Auth>
  );
}
