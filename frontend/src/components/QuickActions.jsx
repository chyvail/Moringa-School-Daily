import React from "react";
import { Link } from "react-router-dom";
import ContentModal from "./ContentModal";
import CategoryModal from "./modals/CategoryModal";
import ProfileModal from "./modals/ProfileModal";

export default function QuickActions() {
  const handleContentSubmit = (id) => {
    const modal = new window.bootstrap.Modal(document.getElementById(id));
    modal.show();
  };
  return (
    <div className="quick-actions pt-2 pb-2">
      <div className="container-lgs quick-links">
        <Link onClick={() => handleContentSubmit("contentModal")}>
          Add New Post
        </Link>
        <Link
          className="ms-3"
          onClick={() => handleContentSubmit("profileModal")}
        >
          Update Profile
        </Link>
        <Link
          className="ms-3"
          onClick={() => handleContentSubmit("categoryModal")}
        >
          Add Category
        </Link>
        <ContentModal />
        <CategoryModal />
        <ProfileModal />
      </div>
    </div>
  );
}
