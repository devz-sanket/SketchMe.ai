import cv2, numpy as np
from PIL import Image

def convert_to_sketch(image: Image.Image) -> Image.Image:
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (13,13), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=240)
    sketch = cv2.addWeighted(sketch, 1.2, np.full_like(sketch,255), -0.2, 0)
    return Image.fromarray(cv2.resize(sketch, (512,512)))
