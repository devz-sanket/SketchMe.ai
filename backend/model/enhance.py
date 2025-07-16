import cv2
import numpy as np
from PIL import Image

def enhance_image_quality(image: Image.Image) -> Image.Image:
    arr = np.array(image.resize((512,512)))
    enhanced = cv2.detailEnhance(arr, sigma_s=10, sigma_r=0.15)
    enhanced = cv2.edgePreservingFilter(enhanced, flags=1, sigma_s=60, sigma_r=0.4)
    return Image.fromarray(enhanced)
