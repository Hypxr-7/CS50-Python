from sys import exit
from datetime import date
import inflect


def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        exit("Invalid Input")

    minutes = total_minutes(birth_date, date.today())
    p = inflect.engine()
    print(f"{p.number_to_words(minutes, andword='').capitalize()} {p.plural('minute', minutes)}")

def total_minutes(date, today):
    return (today - date).days * 24 * 60


if __name__ == "__main__":
    main()

