import React, { useState } from "react";
import "./writeFrom.css"; // Import your CSS file

const WriteForm = () => {
  const [email, setEmail] = useState("");

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // You can add your logic here to handle the email submission
    console.log("Email submitted:", email);
  };

  return (
    <div className="email-form-container">
      <form className="email-form" onSubmit={handleSubmit}>
        <input
          type="email"
          id="email"
          className="email-input"
          placeholder="Enter your email"
          value={email}
          onChange={handleEmailChange}
        />
        <button type="submit" className="submit-button">
          Submit
        </button>
      </form>
    </div>
  );
};

export default WriteForm;
