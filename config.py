IMAGE_DIR = "/mnt/d/pics/image-gallery/images"
# Apache alias for the image directory. This is only necessary if you are not storing your images in the actually Apache DocumentRoot. 
# Leave as "" if this is not the case. Also remember that if you do this you will have to make an Apache alias in the .conf file.
IMAGE_DIR_ALIAS = "images"

THUMB_DIR = "/mnt/d/pics/image-gallery/thumbnails"
THUMB_SIZE = (640, 480)
# Same as image directory alias
THUMB_DIR_ALIAS = "thumbnails"

OUTPUT_DIR = "/mnt/d/comp-sci/projects/image-gallery"

VALID_EXTS = [".jpg", ".jpeg"]
