# file: generate_gallery.py
# A script that generates the index.html file of the image gallery

# third party
import os
import argparse
import sys
import dominate

# mine
import config
import find_images

def generate_album_map(source):
    album_names = sorted(os.listdir(source))

    album_map = dict.fromkeys(album_names, [])
    
    for album_name in album_names:
        full_album_dir = os.path.join(source, album_name)
        images = [os.path.basename(image) for image in find_images.find_images(full_album_dir)]
        album_map[album_name] = images

    return album_map

def generate_div(name, images):
    # this function assumes that the image and its respective thumbnail have the same name
    div = dominate.tags.div(_class="album")

    for image_basename in images:
        image = os.path.join(config.IMAGE_DIR_ALIAS, name, image_basename)
        thumbnail = os.path.join(config.THUMB_DIR_ALIAS, name, image_basename)
        a = div.add(dominate.tags.a(href=thumbnail, _blank=""))
        a.add(dominate.tags.img(src=image, alt="", loading="lazy"))

    return div

def generate_html(album_map):
    html = dominate.tags.html()

    # header
    header = html.add(dominate.tags.header())
    header.add(dominate.tags.title("Balls"))
    header.add(dominate.tags.meta(charset="UTF-8"))
    header.add(dominate.tags.link(rel="stylesheet", href="style.css"))

    # body
    body = html.add(dominate.tags.body())

    for album_name, images in album_map.items():
        body.add(dominate.tags.h1(album_name))
        body.add(generate_div(album_name, images))

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
        "--image-dir", 
        default=config.IMAGE_DIR, 
        help="Directory where the images are stored. Default is specified in config.py."
    )
    parser.add_argument(
        "--output-dir",
        default=config.OUTPUT_DIR,
        help="Directory where the final index.html file will end up. Default is specified in config.py."
    )
    return parser.parse_args()

def main():
    # parse args
    args = parse_args()
    force = args.force
    image_dir = args.image_dir
    output_dir = args.output_dir
    
    # generate the destination directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    index_file = os.path.join(output_dir, "index.html")
    # print(f"Index.html file: {index_file}")
        
    # check if there already is an index.html file
    if os.path.exists(index_file) and not force:
        print(f"Error: index.html already exists at {output_dir}! Use --force to override it.")
        sys.exit(1)

    # a dict where the album name is the key, and all its images are the values as a list
    # Ex: { '2023' : [images/2025/DSC05946.JPG, images/2025/DSC06024.JPG, ...] }
    album_map = generate_album_map(image_dir)

    # main html document
    html = generate_html(album_map)
    print(html.render())

    # write the contents to the file
    # with open(index_file, "w") as f:
    #     f.write(html.render())

if __name__ == "__main__":
    main()