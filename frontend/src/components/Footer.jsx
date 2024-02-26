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
    <footer style={{ backgroundColor: '#212529', color: '#f8f9fa', padding: '2rem 0', marginTop: '100px' }}>
      <div className="container">
        <div className="row">
          <div className="col-lg-4 col-md-6 mb-4 mb-lg-0 d-flex flex-column align-items-center">
            <Logo />
            <p style={{ marginTop: '1.5rem', textAlign: 'center' }}>
              Discover New Opportunities and Expand your Horizons with Our Services!
            </p>
          </div>

          <div className="col-lg-4 col-md-6 mb-4 mb-lg-0 d-flex flex-column justify-content-center align-items-center margin-left-100px" >
            <h3>Contact Us</h3>
            <address>
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
