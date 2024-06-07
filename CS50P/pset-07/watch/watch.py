import re
import sys


# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.search(r".+src=\"(?:https?://(?:www\.)?)?youtube\.com/embed/([\w-]+)\"", s):
        return "https://youtu.be/" + link.group(1)


if __name__ == "__main__":
    main()
