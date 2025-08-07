# file: generate_thumbnails.py
# A script that generates thumbnails for the given images

# third party
import os
import argparse
from PIL import Image

# mine
import config
from directory_scanner import *

def generate_thumbnail(image_path, thumb_size, thumb_name):
    image = Image.open(image_path)
    image.thumbnail(thumb_size)
    image.save(thumb_name)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--image-dir", 
        default=config.IMAGE_DIR, 
        help="Directory where the images are stored. Default is specified in config.py."
    )
    parser.add_argument(
        "--thumb-dir", 
        default=config.THUMB_DIR, 
        help="Directory where the thumbnails are stored. Default is specified in config.py."
    )
    parser.add_argument(
        "--thumb-size", 
        default=config.THUMB_SIZE, 
        nargs=2, metavar=("WIDTH", "HEIGHT"), 
        help="Size in pixels of the generated thumbnails. Default is specified in config.py."
    )
    return parser.parse_args()

def main():
    args = parse_args()
    image_dir = args.image_dir
    thumb_dir = args.thumb_dir
    thumb_size = args.thumb_size

    os.makedirs(thumb_dir, exist_ok=True)

    for dir_name, dir_path in find_dirs(image_dir).items():
        os.makedirs(dir_path, exist_ok=True)

        for image_name, image_path in find_images(dir_path).items():
            thumb_name = os.path.join(thumb_dir, dir_name, image_name)
            generate_thumbnail(image_path, thumb_size, thumb_name)

if __name__ == "__main__":
    main()
