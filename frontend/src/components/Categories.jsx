import React, { useContext, useEffect, useState } from "react";
import { SchoolContext } from "../contexts/SchoolContext";

export default function Categories() {
  const [categories, setCategories] = useState([]);
  const { accessToken } = useContext(SchoolContext);
  useEffect(() => {
    fetch("/categories", {
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => setCategories(data))
      .catch((error) => console.log("error is", error.message));
  }, [accessToken]);
  return (
    <div className="mt-3 container-lgs mb-3">
      {categories &&
        categories.map((category) => (
          <p key={category.id} className="categories mb-0 me-2">
            {category.name}
          </p>
        ))}
    </div>
  );
}
