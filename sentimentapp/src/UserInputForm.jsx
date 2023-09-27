import React, { useRef } from "react";
import "./userInput.css";

const UserInputForm = () => {
  const form = useRef();

  return (
    <div className="select-wrapper">
      <form ref={form}>
        <input
          type="text"
          className="select-dropdown"
          placeholder="Paste your url here"
        />

        <select name="format" id="format" className="select-dropdown">
          <option selected disabled>
            Choose a book format
          </option>
          <li role="option">...</li>
          <li role="option">...</li>
          <option value="pdf">PDF</option>
          <option value="txt">txt</option>
          <option value="epub">ePub</option>
          <option value="fb2">fb2</option>
          <option value="mobi">mobi</option>
        </select>
        <textarea
          type="text"
          className="select-dropdown"
          placeholder="Paste your content here"
          rows="4"
          cols="50"
        />
        <div></div>
      </form>
    </div>
  );
};

export default UserInputForm;
