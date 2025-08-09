# file: generate_thumbnails.py
# A script that generates thumbnails for the given images

# third party
import os
import argparse
from PIL import Image, ImageOps

# mine
from config import *
from directory_scanner import *

def generate_thumbnail(image_path, thumb_size, thumb_name):
    image = Image.open(image_path)
    image = ImageOps.exif_transpose(image)
    image.thumbnail(thumb_size)
    image.save(thumb_name)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-dir", 
        default=SOURCE_DIR, 
        help="The source directory of all the images. Assumes it is in the home directory. Default is specified in config.py."
    )
    parser.add_argument(
        "--image-dir", 
        default=IMAGE_DIR, 
        help="The directory in source where the images are stored. Default is specified in config.py."
    )
    parser.add_argument(
        "--thumb-dir", 
        default=THUMB_DIR, 
        help="The directory in source where the thumbnails will be stored. Default is specified in config.py."
    )
    parser.add_argument(
        "--thumb-size", 
        default=THUMB_SIZE, 
        type=int,
        nargs=2, 
        metavar=("WIDTH", "HEIGHT"), 
        help="Size in pixels of the generated thumbnails. Default is specified in config.py."
    )
    return parser.parse_args()

def main():
    args = parse_args()
    source_dir = args.source_dir
    image_dir = args.image_dir
    thumb_dir = args.thumb_dir
    thumb_size = args.thumb_size

    home_dir = os.getenv("HOME")
    full_image_dir = os.path.join(home_dir, source_dir, image_dir)
    full_thumb_dir = os.path.join(home_dir, source_dir, thumb_dir)

    # make sure thumb_dir exists
    os.makedirs(full_thumb_dir, exist_ok=True)

    for dir_name, dir_path in find_dirs(full_image_dir).items():
        os.makedirs(dir_path, exist_ok=True)

        for image_name, image_path in find_images(dir_path).items():
            thumb_name = os.path.join(full_thumb_dir, dir_name, image_name)
            generate_thumbnail(image_path, thumb_size, thumb_name)

if __name__ == "__main__":
    main()
