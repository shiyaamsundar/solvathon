import React, { useState, useRef } from "react";
import "./fileUpload.css";
import axios from "axios";

function FileUpload({ dragActive, setDragActive

}) {
  const inputRef = useRef(null);
  // const [dragActive, setDragActive] = useState(false);
  // const inputRef = useRef(null);

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleFile = (files) => {
    console.log(files);
    alert("Number of files: " + files.length);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files) {
      handleFile(e.dataTransfer.files);
    }
  };

  const handleChange = (e) => {
    e.preventDefault();
    if (e.target.files && e.target.files[0]) {
      handleFile(e.target.files);
    }
  };

 

  // // const onButtonClick =async(e) => {
  // //   e.preventDefault()
  // //   inputRef.current.click();

  // //   console.log(resp)
  // // };

  // const onButtonClick = async (e) => {
  //   e.preventDefault();

  //   if (handleFile) {
  //     try {
  //       const formData = new FormData();

  //       formData.append("csvFile", handleFile);

  //       const response = await axios.post(
  //         "http://127.0.0.1:8000/upload",

  //         formData,

  //         {
  //           headers: {
  //             "Content-Type": "multipart/form-data",
  //           },
  //         }
  //       );

  //       console.log("File uploaded successfully:", response.data);
  //     } catch (error) {
  //       console.error("Error uploading file:", error);
  //     }
  //   } else {
  //     console.error("No file selected.");
  //   }
  // };

  return (
    <form
      id="form-file-upload"
      onDragEnter={handleDrag}
      onSubmit={(e) => e.preventDefault()}
    >
      <input
        ref={inputRef}
        id="input-file-upload"
        multiple={true}
        onChange={handleChange}
      />
      <label
        id="label-file-upload"
        htmlFor="input-file-upload"
        className={dragActive ? "drag-active" : ""}
      >
        <div className="drop-pdf">
          <p>
            Drag and drop your file here <br />
            <br /> or
          </p>
          <button className="upload-button">Upload a file</button>
        </div>
      </label>
      {dragActive && (
        <div
          id="drag-file-element"
          onDragEnter={handleDrag}
          onDragLeave={handleDrag}
          onDragOver={handleDrag}
          onDrop={handleDrop}
        ></div>
      )}
    </form>
  );
}

export default FileUpload;
