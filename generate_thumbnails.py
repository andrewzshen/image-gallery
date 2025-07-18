import os
import glob
from PIL import Image

thumbnail_size = (300, 300)

years = ["2023", "2024", "2025"]

for year in years:
    images = glob.glob(f"images/{year}/*.JPG")
    for image in images:
        relative_path = os.path.relpath(image, "images")
        im = Image.open(image)
        im.thumbnail(thumbnail_size)
        im.save(f"thumbnails/{relative_path}")