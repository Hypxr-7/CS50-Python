def main():
    var = input("Enter: ")
    print(to_snake_case(var))

def to_snake_case(s):
    new_s = ""
    for c in s:
        if c.isupper():
            new_s += "_" + c.lower()
        else:
            new_s += c
    return new_s

if __name__ == "__main__":
    main()

