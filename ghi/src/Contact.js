import React from "react";
import logoIcon from "./picture/Popcorn.png";

const Contact = () => {
  const emailAddress = "javathescript10@gmail.com";
  const emailSubject = "Regarding Movie Night";

  const handleContactUs = () => {
    window.location.href = `mailto:${emailAddress}?subject=${encodeURIComponent(
      emailSubject
    )}`;
  };

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="row g-0">
          <div className="col-md-4">
            <img
              src={logoIcon}
              alt="Movie Theater"
              className="img-fluid rounded-start"
            />
          </div>
          <div className="col-md-8">
            <div className="card-body">
              <h3 className="card-title">Movie Night</h3>
              <p className="card-text">
                <strong>Email:</strong> {emailAddress}
              </p>
              <p className="card-text">
                <strong>Address:</strong> 1234 Elm Street, Cityville, State, ZIP
              </p>
              <p className="card-text">
                <strong>Owners:</strong> Wilbert Machuca, Constance Basco,
                Nicholas Bailey
              </p>
              <p className="card-text">
                <strong>Incorporation:</strong> Java-the-Script &copy;
              </p>
              <p className="card-text">
                <strong>Mobile:</strong> (305)-123-4567
              </p>
              <button className="btn btn-danger" onClick={handleContactUs}>
                Contact Us
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact;
