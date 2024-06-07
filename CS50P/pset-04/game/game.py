import random

def main():
    level = get_level()
    num = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if num < guess:
                print("Too large!")
            elif 0 < guess < num:
                print("Too small!")
            elif guess <= 0:
                raise ValueError
            else:
                print("Just right!")
                break
        except ValueError:
            pass


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                raise ValueError
            return level
        except ValueError:
            pass


if __name__ == "__main__":
    main()


