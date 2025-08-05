# file: generate_gallery.py
# A script that generates the index.html file of the image gallery

# third party
import os
import argparse
from PIL import Image

# mine
import config
import find_images

def generate_thumbnail(image_path, thumb_size, save_as):
    image = Image.open(image_path)
    image.thumbnail(thumb_size)
    image.save(save_as)

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

    for image in find_images.find_images(image_dir):
        rel_path = os.path.relpath(image, image_dir)
        save_as = os.path.join(thumb_dir, rel_path)
        os.makedirs(os.path.dirname(save_as), exist_ok=True)
        generate_thumbnail(image, thumb_size, save_as)

if __name__ == "__main__":
    main()
