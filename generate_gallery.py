# file: generate_gallery.py
# A script that generates the index.html file of the image gallery

import argparse
import os
import glob
from dominate.tags import *

def generate_anchor(image, thumbnail):
    anchor = a(href=image, target="_blank")
    anchor.add(img(src=thumbnail, alt="", loading="lazy"))
    return anchor

def generate_gallery(image_dir, thumb_dir):
    # this function assumes that the iamge and its respective thumbnail have the same name
    _div = div(_class="gallery")

    images = os.listdir(image_dir)

    for image_name in images:
        image = os.path.join(image_dir, image_name)
        thumbnail = os.path.join(thumb_dir, image_name)
        _div.add(generate_anchor(image, thumbnail))

    return _div

def main():
    # parse args
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--paths",
        action="append", 
        nargs=3,
        metavar=("IMAGE_DIR", "THUMB_DIR", "DIV_TITLE"),
        required=True,
        help="Image and thumbnail directories, followed by the title of the gallery; repeatable."
    )
    args = parser.parse_args()

    # main html document
    _html = html()

    # header
    _header = _html.add(header())
    _header.add(title("Balls"))
    _header.add(meta(charset="UTF-8"))
    _header.add(link(rel="stylesheet", href="style.css"))

    # body
    _body = _html.add(body())

    for image_dir, thumb_dir, div_title in args.paths:
        _body.add(h2(div_title))
        _body.add(generate_gallery(image_dir, thumb_dir))

    # write the contents to the file
    with open("index.html", "w") as f:
        f.write(_html.render())

if __name__ == "__main__":
    main()