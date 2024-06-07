import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1].split(".")[1] != "py":
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1]) as file:
            print("Number of Lines:", get_complexity(file))
    except FileNotFoundError:
        sys.exit("File does not exist")


def get_complexity(file):
    count = 0
    for line in file:
        try:
            if line.strip()[0] != "#":
                count += 1
        except:
            pass
    return count


if __name__ == "__main__":
    main()
