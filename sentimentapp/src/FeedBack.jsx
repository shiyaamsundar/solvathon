import React, { useState } from "react";
import "./feedBack.css";

function FeedbackForm() {
  // State to store user feedback
  const [feedback, setFeedback] = useState("");

  // Function to handle changes in the feedback input
  const handleFeedbackChange = (event) => {
    setFeedback(event.target.value);
  };

  // Function to handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    // You can implement your logic here to send the feedback to a server or perform any other action.
    // For now, let's just log the feedback to the console.
    console.log("User Feedback:", feedback);
    // Optionally, you can reset the input field here:
    setFeedback("");
  };

  return (
    <div className="feedback-container">
      <h2>Give Us Your Feedback</h2>
      <form onSubmit={handleSubmit} className="feedback-form">
        <div className="form-group">
          <label htmlFor="feedback" className="label-feedback">
            Your Feedback:
          </label>
          <textarea
            id="feedback"
            name="feedback"
            rows="4"
            cols="50"
            value={feedback}
            onChange={handleFeedbackChange}
            required
            className="textarea-feedback"
          ></textarea>
        </div>
        <div className="form-group">
          <button type="submit" className="submit-button">
            Submit
          </button>
        </div>
      </form>
    </div>
  );
}

export default FeedbackForm;
