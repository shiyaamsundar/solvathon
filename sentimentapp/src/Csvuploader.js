import React, { useState } from "react";
import axios from "axios";

const CsvUploader = () => {
  const [csvFile, setCsvFile] = useState(null);

  let formData = new FormData();

  const handleFileChange = (event) => {
    const file = event.target.files[0]; // Access the first selected file
    setCsvFile(file);
  };

  const handleUpload = async () => {
    if (csvFile) {
      try {
        formData.append("file", csvFile);
        console.log(formData.get("file"));
        const response = await axios.post(
          "http://localhost:8000/upload",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        console.log("File uploaded successfully:", response.data);
      } catch (error) {
        console.error("Error uploading file:", error.response.data);
      }
    } else {
      console.error("No file selected.");
    }
  };

  return (
    <div>
      <h2>CSV Uploader</h2>
      <input
        type="file"
        name="file"
        accept=".csv"
        onChange={handleFileChange}
      />
      <button onClick={handleUpload}>Upload CSV</button>
    </div>
  );
};

export default CsvUploader;
