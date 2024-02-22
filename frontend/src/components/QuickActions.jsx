import React from "react";
import { Link } from "react-router-dom";
import ContentModal from "./ContentModal";

export default function QuickActions() {
  const handleContentSubmit = () => {
    const modal = new window.bootstrap.Modal(
      document.getElementById("contentModal")
    );
    modal.show();
  };
  return (
    <div className="quick-actions pt-2 pb-2">
      <div className="container-lgs">
        <Link onClick={handleContentSubmit}>Add New Post</Link>
        <ContentModal />
      </div>
    </div>
  );
}
