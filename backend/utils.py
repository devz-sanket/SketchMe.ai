from PIL import Image, ImageFilter, ImageOps
from io import BytesIO
import cv2
import numpy as np
import torch
import torchvision.transforms as T

# Load AnimeGAN2 model
print("🔄 Loading AnimeGAN2 model...")
anime_model = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator").eval()
face2paint = torch.hub.load("bryandlee/animegan2-pytorch:main", "face2paint")

def to_sketch(pil_image):
    image = np.array(pil_image.convert("RGB"))
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Invert and blur to simulate pencil sketch
    inverted = 255 - gray
    blurred = cv2.GaussianBlur(inverted, (21, 21), sigmaX=0, sigmaY=0)

    # Lighter, more natural pencil sketch (scale adjusted)
    sketch = cv2.divide(gray, 255 - blurred, scale=256.0)

    return Image.fromarray(sketch)

def enhance_image(pil_image):
    width, height = pil_image.size

    # Slight upscale to increase quality (1.5x)
    upscale_size = (int(width * 1.5), int(height * 1.5))
    upscaled = pil_image.resize(upscale_size, Image.LANCZOS)

    # Enhance with sharpening and auto contrast
    enhanced = upscaled.filter(ImageFilter.DETAIL)
    enhanced = ImageOps.autocontrast(enhanced)

    return enhanced

def apply_animegan(model, pil_image):
    original_size = pil_image.size

    upscale_size = (768, 768)
    resized = pil_image.resize(upscale_size, Image.LANCZOS)

    transform = T.Compose([
        T.ToTensor(),
        T.Normalize((0.5,), (0.5,))
    ])
    tensor = transform(resized).unsqueeze(0)

    with torch.no_grad():
        out = model(tensor)[0]

    out = (out.clamp(-1, 1) + 1) / 2
    out = out.mul(255).byte().permute(1, 2, 0).cpu().numpy()
    anime_img = Image.fromarray(out)

    anime_img = anime_img.filter(ImageFilter.SHARPEN)
    return anime_img.resize(original_size, Image.LANCZOS)

def transform_image(file_bytes, mode):
    pil_image = Image.open(BytesIO(file_bytes)).convert("RGB")

    if mode == "Image to Sketch":
        return to_sketch(pil_image)
    elif mode == "Human to Painting":
        return apply_animegan(anime_model, pil_image)
    elif mode == "Enhance Image":
        return enhance_image(pil_image)
    else:
        raise ValueError(f"Unsupported mode: {mode}")
