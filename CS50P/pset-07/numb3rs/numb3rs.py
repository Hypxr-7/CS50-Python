import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.search(r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$", ip):
        return False
    
    try:
        if len(ip.split(".")) != 4:
            return False

        for num in ip.split("."):
            if not (0 <= int(num) <= 255):
                return False

        return True

    except ValueError:
        return False


if __name__ == "__main__":
    main()
