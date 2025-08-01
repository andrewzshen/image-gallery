# file: generate_gallery.py
# A script that generates the index.html file of the image gallery

import os
import argparse
import base64
from PIL import Image

def encode_image(image):
    return base64.urlsafe_b64encode(image.encode()).decode() + ".jpg"

def is_valid_ext(f, exts=[".jpg", ".jpeg"]):
    return os.path.splitext(f)[1].lower() in exts

def generate_thumbnail(image, thumb_dir, thumb_size):
    thumbnail = Image.open(image)
    thumbnail.thumbnail(thumb_size)
    encoded_image = os.path.join(thumb_dir, encode_image(image))
    thumbnail.save(encoded_image)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--thumbnail-size", default=(640, 480), help="Size in pixels of the generated thumbnails. Default is (640, 480).")
    parser.add_argument("source", help="Directory where the images are stored; make sure they are organized into proper subdirectories.")
    parser.add_argument("destination", help="Directory where the thumbnails are stored; if they are not in the webserver directory be sure to make a link in the .conf file.")
    return parser.parse_args()

def main():
    args = parse_args()
    thumb_size = args.thumbnail_size
    source = args.source
    destination = args.destination

    os.makedirs(destination, exist_ok=True)

    for root, _, files in os.walk(source):
        for f in files:
            if not is_valid_ext(f):
                continue
            full_path = os.path.join(root, f)
            generate_thumbnail(full_path, destination, thumb_size)

if __name__ == "__main__":
    main()
