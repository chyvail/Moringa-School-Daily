import React from "react";
import signInImage from "../assets/college-students-different-ethnicities-cramming.jpg";
import signUpImage from "../assets/medium-shot-girls-looking-notebook.jpg";
import Logo from "./Logo";
import { useLocation } from "react-router-dom";

export default function Auth({ children }) {
  const location = useLocation();
  const loginExcperpt = `"Join the Community, Explore the Possibilities, Empower Your Tech
  Journey."`;
  const signupExcertpt = `"Connect, Learn, Innovate: Your Tech Adventure Starts Here."`;

  const backgroundImageStyle = {
    backgroundImage: `url(${
      location.pathname === "/login" ? signInImage : signUpImage
    })`,
    backgroundSize: "cover",
    backgroundPosition: "center",
  };

  return (
    <div classNameName="row auth">
      <div classNameName="col-md-7 col-sm-12 auth-image-section" style={backgroundImageStyle}>
        <div
          classNameName="d-flex flex-column justify-content-between"
          style={{ height: "95vh", padding: "2rem" }}
        >
          <div classNameName="mt-4 auth-logo">
            <Logo />
          </div>
          <div classNameName="excerpt">
            <h5>
              {location.pathname === "/login" ? loginExcperpt : signupExcertpt}
            </h5>
          </div>
        </div>
      </div>
      <div classNameName="col-md-5 col-sm-12">
        <div
          classNameName="d-flex flex-column justify-content-center p-3"
          style={{ height: "100vh" }}
        >
          {children}
        </div>
      </div>
    </div>
  );
}
