import requests
import sys

def main():
    try:
        site = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = site.json()
        rate = o["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Request Error")


    try:
        amount = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing Command Line Argument")
    except ValueError:
        sys.exit("Invalid Argument")

    print(f"${amount * rate :,.4f}")




if __name__ == "__main__":
    main()
