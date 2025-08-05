# third party
import os

# mine
import config

def find_images(source):
    images = []
    for root, _, files in os.walk(source):
        for f in files:
            if is_valid_ext(f):
                images.append(os.path.join(root, f))
    return images
    
def is_valid_ext(f):
    return os.path.splitext(f)[1].lower() in config.VALID_EXTS