from tabulate import tabulate
import sys
import csv


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1].split(".")[1] != "csv":
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as file:
            print(tabulate(csv.DictReader(file),
                           headers="keys",
                           tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
