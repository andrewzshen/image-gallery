IMAGE_DIR = "/home/andrew/pictures/image-gallery/images"
# Apache alias for the image directory. This is only necessary if you are not storing your images in the actually Apache DocumentRoot. 
# Leave as "" if this is not the case. Also remember that if you do this you will have to make an Apache alias in the .conf file.
IMAGE_DIR_ALIAS = "images"

# Where the thumbnails are to be stored. If you do not want to use thumbnails, leave as "".
# Similarly, if this directory is in the DocumentRoot, then you do not need an alias and should leave this blank
THUMB_DIR = "/home/andrew/pictures/image-gallery/thumbnails"
THUMB_SIZE = (640, 480)
# Same as image directory alias
THUMB_DIR_ALIAS = "thumbnails"

OUTPUT_DIR = "/var/www/html"

VALID_EXTS = [".jpg", ".jpeg"]
