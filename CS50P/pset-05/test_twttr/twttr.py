def main():
    text = input("Enter: ")
    print(remove_vowels(text))


def shorten(s):
    new_s = ""
    for c in s:
        if c.lower() != "a" and c.lower() != "e" and c.lower() != "i" and c.lower() != "o" and c.lower() != "u":
            new_s += c
    return new_s

if __name__ == "__main__":
    main()

