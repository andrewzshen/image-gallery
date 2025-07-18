import os
import glob
from dominate import document
from dominate.tags import *

years = ["2023", "2024", "2025"]

doc = document("Balls")

with doc.head:
    meta(charset="UTF-8")
    link(rel="stylesheet", href="style.css")

with doc:
    for year in years:
        h1(year)
        with div(_class="gallery"):
            images = glob.glob(f"images/{year}/*.JPG")
            for image in images:
                relative_path = os.path.relpath(image, "images")
                thumbnail = f"thumbnails/{relative_path}"
                with a(href=image, target="_blank"):
                    img(src=thumbnail, alt="", loading="lazy")

with open("index.html", "w") as f:
    f.write(doc.render())