import { Link } from "react-router-dom";
import Auth from "./Auth";
import AuthButton from "./AuthButton";

export default function SignUp() {
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
          <form>
            <div className="mb-3">
              <div className="row gx-1">
                <div className="col-sm-6">
                  <label className="form-label">First Name</label>
                  <input type="text" className="form-control" />
                </div>
                <div className="col-sm-6">
                  <label className="form-label">Last Name</label>
                  <input type="text" className="form-control" />
                </div>
              </div>
            </div>
            <div className="mb-3">
              <label className="form-label">Email address</label>
              <input type="email" className="form-control" />
            </div>
            <div className="mb-3">
              <label className="form-label">Password</label>
              <input type="password" className="form-control" />
            </div>
            <div className="mb-3">
              <label className="form-label">Confirm Password</label>
              <input type="password" className="form-control" />
            </div>
            <AuthButton name="Sign up Here" />
          </form>
        </div>
      </div>
    </Auth>
  );
}
