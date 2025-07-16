import React, { useState } from "react";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import UploadForm from "./components/UploadForm";
import ImageDisplay from "./components/ImageDisplay";
import "./App.css";

const App = () => {
  const BASE_URL = import.meta.env.VITE_API_URL;
  const [imageSrc, setImageSrc] = useState(null);
  const [resultSrc, setResultSrc] = useState(null);

  return (
    <div className="app">
      <video autoPlay loop muted className="bg-video">
  <source
    src="https://videos.pexels.com/video-files/18069701/18069701-uhd_2560_1440_24fps.mp4"
    type="video/mp4"
  />
</video>


      <Navbar />

      <main className="main-container">
        <UploadForm onUpload={setImageSrc} onResult={setResultSrc} />

        {imageSrc && resultSrc && (
          <div className="preview-container">
            <ImageDisplay title="Original Image" src={imageSrc} />
            <ImageDisplay title="Transformed Image" src={resultSrc} download />
          </div>
        )}
      </main>

      <Footer />
    </div>
  );
};

export default App;
