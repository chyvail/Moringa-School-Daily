import React from "react";
import Logo from "./Logo";
import Avatar from "./Avatar";

export default function Nav() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark d-flex justify-content-between p-4">
      <div className="custom-logo">
        <Logo />
      </div>
      <div>
        <ul className="navbar-nav">
          <li className="nav-item dropdown">
            <a
              className="nav-link dropdown-toggle d-flex align-items-center"
              href="/"
              id="navbarDropdownMenuLink"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              <Avatar height={40} alt="User Avatar" />
            </a>
            <ul
              className="dropdown-menu dropdown-menu-end"
              aria-labelledby="navbarDropdownMenuLink"
            >
              <li>
                <a className="dropdown-item" href="/">
                  My profile
                </a>
              </li>
              <li>
                <a className="dropdown-item" href="/">
                  Logout
                </a>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </nav>
  );
}
