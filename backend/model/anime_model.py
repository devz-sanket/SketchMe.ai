import torch
import torchvision.transforms as T
from PIL import Image
# Load animeGAN model using torch.hub
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
anime = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", device=device).eval()
face2paint = torch.hub.load("bryandlee/animegan2-pytorch:main", "face2paint", device=device)

def convert_to_anime(image: Image.Image) -> Image.Image:
    return face2paint(anime, image, side_by_side=False)
