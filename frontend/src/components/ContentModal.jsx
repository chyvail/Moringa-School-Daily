import React, { useContext, useState } from "react";
import { SchoolContext } from "../contexts/SchoolContext";

export default function ContentModal() {
  const { accessToken, userId } = useContext(SchoolContext);
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    content_type: "",
    image_url: "",
    category_id: "",
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
    fetch("/contents", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ...formData, user_id: userId }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.text();
      })
      .then(() => {
        alert("Post added successfully");
        console.log("Post added successfully");
      })
      .catch((error) => {
        console.error("Error adding post:", error.message);
      });
  };

  const handleOnChange = (e) => {
    const key = e.target.id;
    setFormData({ ...formData, [key]: e.target.value });
  };

  return (
    <div
      className="modal fade"
      id="contentModal"
      tabIndex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div className="modal-dialog modal-lg">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title" id="exampleModalLabel">
              Create a New Post 📜
            </h5>
            <button
              type="button"
              className="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div className="modal-body">
            <form onSubmit={handleSubmit}>
              <div className="mb-3">
                <label htmlFor="title" className="col-form-label">
                  Title
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="title"
                  onChange={handleOnChange}
                />
              </div>
              <div className="mb-3">
                <label htmlFor="content_type" className="col-form-label">
                  Content Type
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="content_type"
                  onChange={handleOnChange}
                />
              </div>
              <div className="mb-3">
                <label htmlFor="image_url" className="col-form-label">
                  Image url
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="image_url"
                  onChange={handleOnChange}
                />
              </div>
              <div className="mb-3">
                <label htmlFor="category_id" className="col-form-label">
                  Category
                </label>
                <input
                  type="number"
                  className="form-control"
                  id="category_id"
                  onChange={handleOnChange}
                />
              </div>
              <div className="mb-3">
                <label htmlFor="description" className="col-form-label">
                  Description
                </label>
                <textarea
                  className="form-control"
                  id="description"
                  onChange={handleOnChange}
                ></textarea>
              </div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-secondary"
                  data-bs-dismiss="modal"
                >
                  Close
                </button>
                <button type="submit" className="btn btn-primary">
                  Create Post
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}
