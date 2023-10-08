import React, { useRef, useState } from "react";
import "./userInput.css";
import FileUpload from "./FileUpload";
import axios from "axios";

const UserInputForm = ({ input }) => {
  const form = useRef();
  const [dragActive, setDragActive] = useState(false);

  console.log(input);
  const inputRef = useRef(null);
  const [csvFile, setCsvFile] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0]; // Access the first selected file

    setCsvFile(file);
  };

  const handleUpload = async (e) => {

    e.preventDefault();

    console.log(csvFile,'aaaaa')

    if (csvFile) {
      try {
        const formData = new FormData();

        formData.append("file", csvFile);

        const response = await axios.post(
          "http://127.0.0.1:8000/upload",

          formData,

          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        console.log("File uploaded successfully:", response.data);
      } catch (error) {
        console.error("Error uploading file:", error);
      }
    } else {
      console.error("No file selected.");
    }
  };

  return (
    <div className="select-wrapper">
      <form ref={form}>
        {input == "url" && (
          <input
            type="text"
            className="select-dropdown"
            placeholder="Paste your url here"
          />
        )}
        {input && (
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
        )}

        {input == "text" && (
          <textarea
            type="text"
            className="select-dropdown"
            placeholder="Paste your content here"
            rows="4"
            cols="50"
          />
        )}

        {input == "pdf" && (
          <div className="pdf-upload">
            <input
              type="file"
              name="file"
              accept=".csv"
              onChange={handleFileChange}
            />

            {/* <button onClick={handleUpload}>Upload CSV</button> */}
          </div>
        )}

        <div className="submit-btn">
          {input && (
            <button className="user-sumbit-btn" onClick={handleUpload}>
              submit
            </button>
          )}
        </div>

        <div></div>
      </form>
    </div>
  );
};

export default UserInputForm;
