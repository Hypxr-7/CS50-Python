def main():
    while True:
        try:
            gauge = input("Enter: ")
            num, den = gauge.split("/")
            amount = int(num) / int(den)
            if  0.99 <= amount <= 1.00:
                print("F")
            elif 0 <= amount <= 0.01:
                print("E")
            elif 0.01 < amount < 0.99:
                print(round(amount * 100), "%", sep = "")
            else:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break


if __name__ == "__main__":
    main()
