import React from "react";

export default function Avatar({
  height,
  src = "https://mdbcdn.b-cdn.net/img/Photos/Avatars/img (31).webp",
  alt,
}) {
  return (
    <img
      src={src}
      className="rounded-circle"
      height={height}
      alt={alt}
      loading="lazy"
    />
  );
}
