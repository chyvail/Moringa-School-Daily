import React, { useContext } from "react";
import { SchoolContext } from "../contexts/SchoolContext";

export default function Hero() {
  const { user } = useContext(SchoolContext);
  return (
    <>
      <div className="container-lgs mt-4 hero-top">
        <p>
          Home . <span> Blogs and New Content</span>
        </p>
        <h3>Hello {user || "Guest User"}, Welcome to Moringa Daily</h3>
        <p className="hero-description">
          Access authentic and verified information, inspiration, and advice
          about the tech space.
        </p>
      </div>
      <hr />
    </>
  );
}
