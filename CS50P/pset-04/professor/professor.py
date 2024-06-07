import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        ans = x + y
        for i in range(3):
            print(f"{x} + {y} = ", end="")
            user_ans = input()
            if str(ans) == user_ans:
                score += 1
                break
            else:
                print("EEE")
                if i == 2:
                    print(f"{x} + {y} = {ans}")
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 10**level - 1)
    else:
        return random.randint(10**(level-1), 10**level - 1)



if __name__ == "__main__":
    main()
