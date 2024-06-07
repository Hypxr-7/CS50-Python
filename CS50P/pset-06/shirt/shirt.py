import sys
from PIL import Image, ImageOps
import os

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    valid_ext = [".jpg", ".jpeg", ".png"]
    if os.path.splitext(sys.argv[1])[1].lower() not in valid_ext or os.path.splitext(sys.argv[2])[1].lower() != os.path.splitext(sys.argv[1])[1].lower():
        sys.exit("Invalid File Format")

    try:
        shirt_im = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as im:
            im = ImageOps.fit(im, shirt_im.size)
            im.paste(shirt_im, shirt_im)
            im.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]} does not exist")


if __name__ == "__main__":
    main()
