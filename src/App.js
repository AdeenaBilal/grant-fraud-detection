import './App.css';  // or './FileUpload.css' if you named it that

import React, { useState } from "react";

export default function FileUpload() {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      // ---- Posting data to Grantees table ---- //
      const granteeResponse = await fetch(
        "http://127.0.0.1:5000/api/upload-grantees",
        {
          method: "POST",
          body: formData,
        }
      );

      const granteeData = await granteeResponse.json();
      if (!granteeResponse.ok) {
        alert("Grantee upload failed: " + granteeData.message);
        return;
      }

      // ---- Posting data to Applications table ---- //
      const appResponse = await fetch(
        "http://127.0.0.1:5000/api/upload-application",
        {
          method: "POST",
          body: formData,
        }
      );

      const appData = await appResponse.json();
      if (!appResponse.ok) {
        alert("Application upload failed: " + appData.message);
        return;
      }

      // If both succeeded
      alert(
        "Grantees uploaded: " +
          granteeData.message +
          "\nApplications uploaded: " +
          appData.message
      );
    } catch (err) {
      console.error(err);
      alert("Upload failed! See console for details.");
    }
  };

  return (
    <div className="upload-container">
      <h2>Upload Grantee File</h2>
      <input type="file" accept=".csv" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );

}
