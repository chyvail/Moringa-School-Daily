import React from "react";
import customImage from "../assets/college-students-different-ethnicities-cramming.jpg";
import Logo from "./Logo";

export default function Auth({ children }) {
  const backgroundImageStyle = {
    backgroundImage: `url(${customImage})`,
    backgroundSize: "cover",
    backgroundPosition: "center",
  };

  return (
    <div className="row auth">
      <div className="col-sm-8" style={backgroundImageStyle}>
        <div
          className="d-flex flex-column justify-content-between"
          style={{ height: "95vh", padding: "2rem" }}
        >
          <div className="mt-4 auth-logo">
            <Logo />
          </div>
          <div className="excerpt">
            <h5>
              "Join the Community, Explore the Possibilities, Empower Your Tech
              Journey."
            </h5>
          </div>
        </div>
      </div>
      <div className="col-sm-4">
        <div
          className="d-flex flex-column justify-content-center p-3"
          style={{ height: "100vh" }}
        >
          {children}
        </div>
      </div>
    </div>
  );
}
