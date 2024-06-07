def main():
    months = [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ]

    while True:
        date = input("Enter:")
        try:
            m, d, y = date.split("/")
            if int(m) > 12 or int(d) > 31:
                raise ValueError
            print(f"{int(y):04}-{int(m):02}-{int(d):02}")
            break
        except ValueError:
            pass

        try:
            m, d, y = date.split(" ")
            if m not in months or int(d.replace(",","")) > 31 or d.find(",") == -1:
                raise ValueError
            print(f"{int(y):04}-{months.index(m) + 1:02}-{int(d.replace(",", "")):02}")
            break
        except ValueError:
            pass




if __name__ == "__main__":
    main()
