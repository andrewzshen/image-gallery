# file: generate_gallery.py
# A script that generates the index.html file of the image gallery

# third party
import os
import argparse
import sys
import dominate

def is_image_file(f, exts=[".jpg", ".jpeg"]):
    return os.path.splitext(f)[1].lower() in exts

def generate_album_map(source):
    # the apache alias for the image directory
    source_alias = "/gallery"

    albums = sorted(
        [f for f in os.scandir(source) if f.is_dir()],
        key=lambda x: x.name
    )

    album_map = {}

    for album in albums:
        images = [os.path.join(source_alias, album.name, f) for f in os.listdir(album.path) if is_image_file(f)]
        album_map[album.name] = images
    
    return album_map

def generate_div(images):
    # this function assumes that the iamge and its respective thumbnail have the same name
    album_div = dominate.div(_class="album")

    for image in images:
        album_div.add(dominate.img(src=image, alt="", loading="lazy"))

    return album_div

def generate_html(album_map):
    html = dominate.html()

    # header
    header = html.add(dominate.header())
    header.add(dominate.title("Balls"))
    header.add(dominate.meta(charset="UTF-8"))
    # _header.add(link(rel="stylesheet", href="style.css"))

    # body
    body = html.add(dominate.body())

    for album_name, images in album_map.items():
        body.add(dominate.h1(album_name))
        body.add(generate_div(images))

    return html

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--force", action="store_true", help="Override existing index.html if one exists.")
    parser.add_argument("source", help="Directory where the images are stored; make sure they are organized into proper subdirectories.")
    parser.add_argument("destination", help="Directory where the final index.html file will end up.")
    return parser.parse_args()

def main():
    # parse args
    args = parse_args()
    source = args.source
    destination = args.destination
    force = args.force
    
    # generate the destination directory if it does not exist
    if not os.path.exists(destination):
        os.makedirs(destination, exist_ok=True)

    index_file = os.path.join(destination, "index.html")
    # print(f"Index.html file: {index_file}")
        
    # check if there already is an index.html file
    if os.path.exists(index_file) and not force:
        print(f"Error: index.html already exists at {destination}! Use --force to override it.")
        sys.exit(1)

    # a dict where the album name is the key, and all its images are the values as a list
    # So ex: { '2023' : [/gallery/2025/DSC05946.JPG, /gallery/2025/DSC06024.JPG, ...] }
    album_map = generate_album_map(source)

    # main html document
    html = generate_html(album_map)
    print(html.render())

    # write the contents to the file
    with open(index_file, "w") as f:
        f.write(html.render())

if __name__ == "__main__":
    main()