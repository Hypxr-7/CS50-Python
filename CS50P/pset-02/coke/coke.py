def main():
    total = 0
    while total < 50:
        print("Amount Due:", 50 - total)
        coin = int(input("Insert Coin: "))
        if coin == 5 or coin == 10 or coin == 25:
            total += coin
    print("Change Owed:", total - 50)

if __name__ == "__main__":
    main()
