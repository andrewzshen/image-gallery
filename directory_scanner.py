# file: directory_scanner.py
# A helper script that provides some functions for traversing the image directory

# third party
import os

# mine
import config

def find_images(image_dir):
    images = {}
    for entry in os.scandir(image_dir):
        if entry.is_file() and is_valid_ext(entry.name):
            images[entry.name] = entry.path
    return images

def find_dirs(image_dir):
    dirs = {}
    for entry in os.scandir(image_dir):
        if entry.is_dir():
            dirs[entry.name] = entry.path
    return dict(sorted(dirs.items()))
    
def is_valid_ext(f):
    return os.path.splitext(f)[1].lower() in config.VALID_EXTS