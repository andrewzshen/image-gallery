# file: generate_gallery.py
# A script that generates the index.html file of the image gallery

# third party
import os
import argparse
import sys
import dominate

# mine
from config import *
from directory_scanner import *

def generate_album_map(image_dir):
    album_names = sorted(os.listdir(image_dir))

    album_map = dict.fromkeys(album_names, [])
    
    for album_name in album_names:
        full_album_dir = os.path.join(image_dir, album_name)
        images = [os.path.basename(image) for image in find_images(full_album_dir)]
        album_map[album_name] = images

    return album_map

def generate_html(source_dir, image_dir, thumb_dir):
    full_image_dir = os.path.join(os.getenv("HOME"), source_dir, image_dir)

    # a dict where the album name is the key, and all its images are the values as a list
    # Ex: { '2023' : [images/2025/DSC05946.JPG, images/2025/DSC06024.JPG, ...] }
    album_map = generate_album_map(full_image_dir)

    html = dominate.tags.html()

    # head
    head = html.add(dominate.tags.head())
    head.add(dominate.tags.title("Andrew's Balls"))
    head.add(dominate.tags.meta(charset="UTF-8"))
    head.add(dominate.tags.link(rel="stylesheet", href="style.css"))

    # body
    body = html.add(dominate.tags.body())

    # tab links div
    tab = body.add(dominate.tags.div(_class="tab"))

    for album_name in album_map.keys():
        tab.add(dominate.tags.button(album_name, _class="tablink", onclick=f"openTab(event, '{album_name}')"))

    for album_name, images in album_map.items():
        # tab content div
        tab_content = body.add(dominate.tags.div(id=album_name, _class="tabcontent"))

        # header
        tab_content.add(dominate.tags.h1(album_name))

        for image_name in images:
            image = os.path.join(WEB_DIR_ALIAS, image_dir, album_name, image_name)
            thumbnail = os.path.join(WEB_DIR_ALIAS, thumb_dir, album_name, image_name)
            
            # anchor  
            anchor = tab_content.add(dominate.tags.a(href=image, target="_blank"))
            anchor.add(dominate.tags.img(src=thumbnail, alt="", loading="lazy"))
    
    # script
    body.add(dominate.tags.script(type="text/javascript", src="tabs.js"))

    return html

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--force", 
        action="store_true",
        default=False,
        help="Override existing index.html if one exists."
    )
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
        help="The directory in source where the thumbnails are stored. Default is specified in config.py."
    )
    return parser.parse_args()

def main():
    # parse args
    args = parse_args()
    force = args.force
    source_dir = args.source_dir
    image_dir = args.image_dir
    thumb_dir = args.thumb_dir
        
    # check if there already is an index.html file
    if os.path.exists("index.html") and not force:
        print(f"Error: index.html already exists in currently working directory! Use --force to override it.")
        sys.exit(1)

    # main html document
    html = generate_html(source_dir, image_dir, thumb_dir)
    print(html.render())

    # write the contents to the file
    with open("index.html", "w") as f:
        f.write(html.render())

if __name__ == "__main__":
    main()