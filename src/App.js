// FileUpload.js
import React, { useState } from "react";

function FileUpload() {
  const [file, setFile] = useState(null);

  // Triggered when user selects a file
  const handleFileChange = (event) => {
    setFile(event.target.files[0]); // Save the first selected file
  };

  // Triggered when user clicks "Upload"
  const handleUpload = () => {
    if (!file) {
      alert("Please select a file first!");
      return;
    }

    // For now, just log the file info
    console.log("Selected file:", file);

    // Later: send file to backend using fetch or axios
    // Example:
    // const formData = new FormData();
    // formData.append("file", file);
    // fetch("/api/upload", { method: "POST", body: formData });
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Upload a File</h2>
      <input type="file" onChange={handleFileChange} />
      <br /><br />
      <button onClick={handleUpload}>Upload</button>
      {file && (
        <div style={{ marginTop: "10px" }}>
          <strong>Selected File:</strong> {file.name}
        </div>
      )}
    </div>
  );
}

export default FileUpload;
