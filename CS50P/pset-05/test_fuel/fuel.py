def main():
    fraction = input("Enter: ")
    print(gauge(convert(fraction)))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
    except ValueError:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError

    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
