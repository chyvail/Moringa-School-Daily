import React from "react";
import Avatar from "./Avatar";
import AuthButton from "./AuthButton";

export default function Comments({ comments }) {
  return (
    <div className="comments-posting">
      <div className="d-flex justify-content-center">
        <div className="comments-icons ">
          <i
            className="fa-solid fa-comment-dots"
            data-bs-toggle="offcanvas"
            data-bs-target="#offcanvasRight"
          ></i>
          <p className="comments ms-1">{comments.length}</p>
        </div>
        <div className="comments-icons ms-3">
          <i className="fa-solid fa-thumbs-up"></i>
          <p className="comments ms-1">5</p>
        </div>
        <div className="comments-icons ms-3">
          <i className="fa-solid fa-floppy-disk"></i>
          <p className="comments ms-1">5</p>
        </div>
      </div>
      <div
        className="offcanvas offcanvas-end"
        tabIndex="-1"
        id="offcanvasRight"
        aria-labelledby="offcanvasRightLabel"
      >
        <div className="offcanvas-header">
          <h5 className="offcanvas-title" id="offcanvasRightLabel">
            Comments ({comments.length})
          </h5>
          <button
            type="button"
            className="btn-close"
            data-bs-dismiss="offcanvas"
            aria-label="Close"
          ></button>
        </div>
        <div className="offcanvas-body">
          <Avatar height={40} />
          <strong>Joshua Omwami Smith</strong>
          <div className="mt-3">
            <textarea
              className="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
              placeholder="What are your Thoughts"
              required
            />
          </div>
          <div className="mt-3">
            <AuthButton name="Comment" />
          </div>
          <hr />
          {comments.length > 0
            ? comments.map((comment,index) => (
                <div key={index}>
                  <p className="mb-0">{comment.comment}</p>
                  <p className="comment-user mt-0">~ By {comment.user}</p>
                </div>
              ))
            : "No comments Available"}
        </div>
      </div>
    </div>
  );
}
