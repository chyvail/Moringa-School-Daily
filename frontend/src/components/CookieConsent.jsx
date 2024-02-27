import React, { useState, useEffect } from 'react';

const MyComponent = () => {
  const [showCookieConsent, setShowCookieConsent] = useState(true);

  useEffect(() => {
    const handleAccept = () => {
      setShowCookieConsent(false); // Hide the cookie consent message
    };

    const script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'https://cookieconsent.popupsmart.com/src/js/popper.js';
    document.body.appendChild(script);

    // Initialize the cookie consent if window.start object exists
    if (window.start) {
      window.start.init({
        Palette: "palette4",
        Mode: "banner bottom",
        Theme: "classic",
        onAccept: handleAccept // Callback function when the user accepts the cookie
      });
    }

    return () => {
      // Cleanup: remove the script when the component unmounts
      document.body.removeChild(script);
    };
  }, []); // Empty dependency array ensures that this effect runs only once

  const handleAccept = () => {
    setShowCookieConsent(false); // Hide the cookie consent message
  };

  return (
    <div>
      {showCookieConsent && (
        <div className="cookie-consent">
          <p>
            We use cookies to enhance your user experience. By using our website,
            you agree to our use of cookies.{' '}
            <a href="/privacy-policy">Learn more.</a>
          </p>
          <button onClick={handleAccept}>
            Accept
          </button>
        </div>
      )}
    </div>
  );
};

export default MyComponent;
