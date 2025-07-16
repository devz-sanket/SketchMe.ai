import React from "react";
import "./ImageDisplay.css";

const ImageDisplay = ({ src, title, download }) => {
  return (
    <div className="image-display">
      <h3>{title}</h3>
      <img src={src} alt={title} />
      {download && (
        <a href={src} download="transformed.png" className="download-btn">
          Download
        </a>
      )}
    </div>
  );
};

export default ImageDisplay;
