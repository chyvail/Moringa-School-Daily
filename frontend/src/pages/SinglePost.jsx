// SinglePost.js
import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Nav from "../components/Nav";
import Avatar from "../components/Avatar";

export default function SinglePost() {
  const { id } = useParams();
  const [post, setPost] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`/contents/${id}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch post");
        }
        return response.json();
      })
      .then((data) => {
        setPost(data);
      })
      .catch((error) => {
        setError(error.message);
      });
  }, [id]);

  if (error) {
    return <p>Error: {error}</p>;
  }

  if (!post) {
    return <p>Loading...</p>;
  }

  return (
    <>
      <Nav />
      <div className="container-lgs single-post">
        <div className="text-center">
          <p className="mb-0">
            {post.category_id}
            <span> . 5 min read</span>
          </p>
          <h3>{post.title}</h3>
          <Avatar height={40}/>
        </div>
        <p className="text-center mt-5">{post.description}</p>
      </div>
    </>
  );
}
