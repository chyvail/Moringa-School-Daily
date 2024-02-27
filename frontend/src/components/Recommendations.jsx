// Recommendations.jsx
import React, { useState, useEffect, useContext } from 'react';
import { Link } from 'react-router-dom';
import { SchoolContext } from '../contexts/SchoolContext';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import CookieConsent from './CookieConsent';

const Recommendations = () => {
  const { accessToken, userId } = useContext(SchoolContext);
  const [showRecommendations, setShowRecommendations] = useState(false);
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    const isCookieAccepted = localStorage.getItem('cookieAccepted');
    if (isCookieAccepted === 'true') {
      fetchRecommendations();
    }
  }, []);

  const handleAcceptCookie = () => {
    localStorage.setItem('cookieAccepted', 'true');
    setShowRecommendations(true);
    fetchRecommendations();
  };

  const fetchRecommendations = async () => {
    try {
      const response = await fetch('/recommendations', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`
        },
      });
      if (response.ok) {
        const data = await response.json();
        setRecommendations(data);
      } else {
        console.error('Failed to fetch recommendations');
      }
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    }
  };

  const handleDelete = (id) => {
    console.log("Clicked post with id", id);
    fetch(`/contents/${id}`, {
      method: "DELETE",
      headers: { Authorization: `Bearer ${accessToken}` },
    })
      .then(() => {
        toast.success("Post deleted Successfully", {
          position: "bottom-center",
        });
      })
      .catch((error) => {
        console.error("Delete post failed:", error.message);
        toast.error("Post deletion Failed", {
          position: "bottom-center",
        });
      });
  };

  return (
    <div>
      <CookieConsent onAccept={handleAcceptCookie} />
      {showRecommendations && (
        <div className="recommendations">
          <h2>Recommendations</h2>
          <div className="row g-3">
            {recommendations.length > 0 ? (
              recommendations.map(recommendation => (
                <div key={recommendation.id} className="col-sm-12 col-md-6 col-lg-4 blog-image mb-2">
                  <img src={recommendation.image_url} alt="" />
                  <p className="mt-3">
                    {recommendation.category_id}
                    <span> . 5 min read</span>
                  </p>
                  <Link to={`/posts/${recommendation.id}`}>
                    <h4 className="post-title">{recommendation.title}</h4>
                  </Link>
                  <p className="post-description">{recommendation.description}</p>
                  <div className="custom-avatar d-flex align-items-center justify-content-between">
                    <div>
                      <strong>{`${recommendation.added_by.firstname} ${recommendation.added_by.lastname}`}</strong>
                    </div>
                    <div className="trash">
                      {userId === recommendation.added_by.user_id ? (
                        <i className="fa-solid fa-trash-can primary" onClick={() => { handleDelete(recommendation.id); }}></i>
                      ) : null}
                    </div>
                  </div>
                </div>
              ))
            ) : (
              <div className="text-center">
                No recommendations available.
              </div>
            )}
          </div>
        </div>
      )}
      <ToastContainer />
    </div>
  );
};

export default Recommendations;
