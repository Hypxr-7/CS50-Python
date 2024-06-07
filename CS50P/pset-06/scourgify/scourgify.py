import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if sys.argv[1].split(".")[1] != "csv" or sys.argv[2].split(".")[1] != "csv":
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as input:
            with open(sys.argv[2], "w") as output:
                reader = csv.DictReader(input)
                writer = csv.DictWriter(output, fieldnames=["first",
                                                            "last",
                                                            "house"])
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].strip().split(", ")
                    writer.writerow({"first" : first,
                                    "last" : last,
                                    "house" : row["house"]})
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]} does not exist")


if __name__ == "__main__":
    main()
