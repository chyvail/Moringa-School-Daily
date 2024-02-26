import React, { useContext } from "react";
import { SchoolContext } from "../contexts/SchoolContext";
import { useLocation } from "react-router-dom";

export default function Hero() {
  const { user } = useContext(SchoolContext);
  const location = useLocation();
  return (
    <>
      <div className="container-lgs mt-4 hero-top">
        {location.pathname === "/" ? (
          <>
            <p>
              Home . <span> Blogs and New Content</span>
            </p>
            <h3>Hello {user || "Guest User"}, Welcome to Moringa Daily</h3>
            <p className="hero-description">
              Access authentic and verified information, inspiration, and advice
              about the tech space.
            </p>
          </>
        ) : (
          <>
            <p>
              Dashboard . <span> Admin's Den</span>
            </p>
            <h3>Hey there, Admin Extraordinaire!</h3>
            <p className="hero-description">
              Welcome to the command center of Moringa Daily, where you wield
              the power to curate the digital realm.
            </p>
          </>
        )}
      </div>
      <hr />
    </>
  );
}
