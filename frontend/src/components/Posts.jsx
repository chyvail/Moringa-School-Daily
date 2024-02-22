import React, { useState, useEffect } from "react";
import Avatar from "./Avatar";

export default function Posts() {
  const [postData, setPostData] = useState(null);
  const [error, setError] = useState(null);
  const img_url =
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=2944&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D";

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
        {postData &&
          postData.map((post) => (
            <div key={post.title}className="col-sm-12 col-md-6 col-lg-4 blog-image">
              <img src={img_url} alt="" />
              <p className="mt-3">
                {post.category_id}
                <span> . 5 min read</span>
              </p>
              <h4 className="post-title">{post.title}</h4>
              <p className="post-description">{post.description}</p>
              <div className="custom-avatar">
                <Avatar height={40} alt="User Avatar" />
              </div>
            </div>
          ))}
      </div>
    </div>
  );
}
