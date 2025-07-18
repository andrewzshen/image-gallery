import os

image_directory = "images"
years = ["2023", "2024", "2025"]

# names of title and header
title = "Balls"
header1 = "Pictures"

f = open("index.html", "w")
f.write(
f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>{header1}</h1>
'''
)

for year in years:
    f.write(f"<h2>{year}</h2>\n<div class='gallery'>\n")
    directory_path = os.path.join(image_directory, year)
    image_count = 0

    for image in sorted(os.listdir(directory_path)):
        if image.lower().endswith((".jpg", ".jpeg")):
            image_path = os.path.join(directory_path, image)
            image_path.replace("\\", "/")
            f.write(f"<img src='{image_path}' alt=''>\n")
        image_count += 1
    
    f.write("</div>\n")
    print(f"{year} image count: {image_count}")

f.write("</body>\n</html>")