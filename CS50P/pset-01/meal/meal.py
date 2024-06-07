def main():
    time = input("Enter Time: ")
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")


def convert(time):
    if time.find("a.m.") != -1 or time.find("p.m.") != -1:
        time = convert_format(time)
    min = time[time.find(":") + 1 :]
    return int(time[: time.find(":")]) + float(min)/60


def convert_format(time):
    if time.find("a.m.") != -1:
        return time[: time.find(" ")]

    min = time[time.find(":") + 1 : time.find(" ")]
    hr =  int(time[: time.find(":")]) + 12
    return str(hr) + ":" + min


if __name__ == "__main__":
    main()
