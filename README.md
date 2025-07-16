SketchMe.ai — AI-Powered Image Tool

FIRSTLY VIEW README.txt to run the project.

SketchMe.ai is a full-stack AI-powered web tool that transforms your images into:

- Pencil Sketches  
- Anime-style Paintings  
- Enhanced High-Quality Versions  

Built using React + Vite (Frontend) and FastAPI + OpenCV + AnimeGAN (Backend).


Features

- Drag and Drop Image Upload
- Modes: Sketch, Human-to-Anime, Image Enhancer
- Real-time Preview: Original vs Transformed Image
- Beautiful UI with Background Video & Animations
- Responsive & Modern Design
- Download Transformed Images
  
How It Works
Upload Image via drag-and-drop or file picker.

Choose mode:

Image to Sketch: uses OpenCV to generate pencil sketch.

Human to Anime: uses pretrained AnimeGAN model to convert portrait.

Enhance Image: increases resolution to 1024x1024 (optionally supports super-resolution).

FastAPI processes the image and sends the transformed version back.

React frontend shows preview + download option.
