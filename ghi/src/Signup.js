import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Signup = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [first, setFirst] = useState("");
  const [last, setLast] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/api/accounts", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password, first, last }),
      });

      if (!response.ok) {
        throw new Error("Failed to create an account with those credentials.");
      }

      const data = await response.json();

      console.log(data);
      setError("");

      navigate("/");
    } catch (error) {
      setError("Failed to create an account with those credentials.");
      console.error(error);
    }
  };

  return (
    <div className="container mt-5 bg-white p-4 rounded shadow">
      <h2>Sign Up</h2>
      <form onSubmit={handleFormSubmit}>
        <div className="form-group">
          <label>Email:</label>
          <input
            type="email"
            className="form-control"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>Password:</label>
          <input
            type="password"
            className="form-control"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>First Name:</label>
          <input
            type="text"
            className="form-control"
            value={first}
            onChange={(e) => setFirst(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>Last Name:</label>
          <input
            type="text"
            className="form-control"
            value={last}
            onChange={(e) => setLast(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <button type="submit" className="btn btn-primary">
            Sign Up
          </button>
        </div>
      </form>
      {error && <p className="text-danger">{error}</p>}
    </div>
  );
};

export default Signup;
