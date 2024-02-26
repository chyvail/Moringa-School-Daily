import React from "react";
import bloggerImage from "../assets/blogger.png"; 

export default function Stats() {
  const statsData = [
    { label: "No of Users", image: bloggerImage, count: 100 },
    { label: "No of Posts", image: bloggerImage, count: 100 },
    { label: "No of Admins", image: bloggerImage, count: 100 },
    { label: "No of TechWriters", image: bloggerImage, count: 100 }
  ];

  return (
    <div className="mt-3 container-lgs">
      <p>Stats</p>
      <div className="row gx-2">
        {statsData.map((stat, index) => (
          <div className="col-sm-3 stats" key={index}>
            <div className={`p-3 bg-light ${stat.label.toLowerCase()} rounded-3 d-flex align-items-center`}>
              <div className="d-flex flex-column">
                {stat.label}
                <img src={stat.image} alt="" className="mt-1" />
              </div>
              <div className="digits">{stat.count}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
