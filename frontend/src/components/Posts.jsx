import React, { useState, useEffect } from "react";
import Avatar from "./Avatar";
import { Link } from "react-router-dom";

export default function Posts() {
  const [postData, setPostData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("/contents")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        return response.json();
      })
      .then((data) => {
        setPostData(data);
      })
      .catch((error) => {
        setError(error.message);
      });
  }, []);

  return (
    <div className="container-lgs hero-top">
      <p>All Blog Posts</p>
      <div className="row">
        {error && <p>{error}</p>}
        {postData.length > 0 ? (
          postData.map((post) => (
            <div
              key={post.title}
              className="col-sm-12 col-md-6 col-lg-4 blog-image"
            >
              <img src={post.image_url} alt="" />
              <p className="mt-3">
                {post.category_id}
                <span> . 5 min read</span>
              </p>
              <Link to={`/posts/${post.id}`}><h4 className="post-title">{post.title}</h4></Link>
              <p className="post-description">{post.description}</p>
              <div className="custom-avatar">
                <Avatar height={40} alt="User Avatar" />{" "}
                <strong>{`${post.added_by.firstname} ${post.added_by.lastname}`}</strong>
              </div>
            </div>
          ))
        ) : (
          <div className="text-center">
            No posts Available. Create one by clicking on 
            <span>Add New Post</span>
          </div>
        )}
      </div>
    </div>
  );
}
