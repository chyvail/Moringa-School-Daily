import React, { useContext } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faWhatsapp, faTwitter, faFacebook, faInstagram } from '@fortawesome/free-brands-svg-icons';
import Logo from './Logo';
import { SchoolContext } from '../contexts/SchoolContext';
import { useNavigate } from 'react-router-dom';

const Footer = () => {
  const { userEmail, userRole, setUser } = useContext(SchoolContext);
  const history = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('accessToken');
    setUser('');
    history('/login');
  };

  const handleWhatsAppClick = () => {
    window.open('https://wa.me/254792172462', '_blank');
  };

  const handleTwitterClick = () => {
    window.open('https://twitter.com/moringadaily', '_blank');
  };

  const handleFacebookClick = () => {
    window.open('https://facebook.com/moringadaily', '_blank');
  };

  const handleInstagramClick = () => {
    window.open('https://instagram.com/moringadaily', '_blank');
  };

  return (
    <footer style={{ backgroundColor: '#212529', color: '#f8f9fa', padding: '2rem 0',marginTop: '100px' }}>
      <div className="container">
        <div className="row">
          <div className="col-lg-4 col-md-6 mb-4 mb-lg-0">
            <Logo style={{ color: 'black', marginLeft: '-15px' }} />
            <p style={{ marginTop: '1.5rem' }}>
              Discover New Opportunities and Expand your Horizons with Our Services!
            </p>
          </div>
          <div className="col-lg-3 col-md-6 mb-4 mb-lg-0">
            <h3>Quick Links</h3>
            <ul className="list-unstyled mb-0">
              <li><a href="/" style={{ fontSize: '1.2rem', fontFamily: 'Arial, sans-serif' }}>Home</a></li>
              <li><a href="/about" style={{ fontSize: '1.2rem', fontFamily: 'Arial, sans-serif' }}>About Us</a></li>
            </ul>

          </div>
          <div className="col-lg-3 col-md-6 mb-4 mb-lg-0">
            <h3>Early Access</h3>
            <div className="dropdown">
              <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Stay Updated To Favouriites
              </button>
              <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <a className="dropdown-item" href="/">CyberSecurity</a>
                <a className="dropdown-item" href="/">Web Development</a>
                <a className="dropdown-item" href="/">Software Engineering</a>
                <a className="dropdown-item" href="/">Machine Learning</a>
              </div>
            </div>
          </div>
          <div className="col-lg-2 col-md-6 mb-4 mb-lg-0">
            <h3>Contact Us</h3>
            <address>
              <p><strong>Address:</strong> Nairobi, Ngomng Road</p>
              <p><strong>Email:</strong> stngsng386@gmail.com</p>
              <p><strong>Phone:</strong> +254 792 172 462</p>
              <a href="https://wa.me/254792172462" target="_blank" rel="noopener noreferrer"><FontAwesomeIcon icon={faWhatsapp} onClick={handleWhatsAppClick} style={{ marginRight: '20px', fontSize: '2rem', color: '#f8f9fa' }} /></a>
              <a href="https://twitter.com/moringadaily" target="_blank" rel="noopener noreferrer"><FontAwesomeIcon icon={faTwitter} style={{ marginRight: '20px', fontSize: '2rem', color: '#f8f9fa' }} /></a>
              <a href="https://facebook.com/moringadaily" target="_blank" rel="noopener noreferrer"><FontAwesomeIcon icon={faFacebook} style={{ marginRight: '20px', fontSize: '2rem', color: '#f8f9fa' }} /></a>
              <a href="https://instagram.com/moringadaily" target="_blank" rel="noopener noreferrer"><FontAwesomeIcon icon={faInstagram} style={{ fontSize: '2rem', color: '#f8f9fa' }} /></a>
            </address>
          </div>
        </div>
      </div>
      <div style={{ backgroundColor: '#212529', color: '#f8f9fa', padding: '1.5rem 0' }}>
        <div className="container text-center">
          <p>&copy; {new Date().getFullYear()} Moringa Daily. All rights reserved. For support, contact support@moringadaily.com</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
