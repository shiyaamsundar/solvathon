import React, { useRef, useState } from "react";
import "./userInput.css";
import FileUpload from "./FileUpload";
import axios from "axios";
import { useEffect } from "react";

const UserInputForm = ({ input }) => {
  const form = useRef();
  const [articleurl, setarticleurl] = useState(null)
  const [newstext, setnewstext] = useState('')
  const [ticker, setticker] = useState('')

  console.log(input);
  const inputRef = useRef(null);
  const [csvFile, setCsvFile] = useState(null);

  useEffect(() => {
   
  }, [input])
  

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
          `http://127.0.0.1:8000/upload/csv/${ticker}/${csvFile.name}`,
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

    if(input == "url")
    {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/url', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ articleurl, ticker }),
        });

    }
    catch(e){
      console.log(e)
    }
  }

    if(input=='text')
    {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/text', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ newstext, ticker }),
        });

    }
    catch(e){
      console.log(e)
    }
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
            onChange={(e)=>setarticleurl(e.target.value)}
          />
        )}
        {input && (
          <input
            type="text"
            className="select-dropdown"
            placeholder="Please enter you picker name"
            onChange={(e)=>setticker(e.target.value)}
          />
        )}

        {input == "text" && (
          <textarea
            type="text"
            className="select-dropdown"
            placeholder="Paste your content here"
            rows="4"
            cols="50"
            onChange={(e)=>setnewstext(e.target.value)}
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
