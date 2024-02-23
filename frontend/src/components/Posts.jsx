import React, { useState, useEffect, useContext } from "react";
import Avatar from "./Avatar";
import { Link } from "react-router-dom";
import { SchoolContext } from "../contexts/SchoolContext";

export default function Posts() {
  const { postData } = useContext(SchoolContext);

  return (
    <div className="container-lgs hero-top">
      <p>All Blog Posts</p>
      <div className="row">
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
              <Link to={`/posts/${post.id}`}>
                <h4 className="post-title">{post.title}</h4>
              </Link>
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
