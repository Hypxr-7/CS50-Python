def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return min_letter_check(s) and length_check(s) and num_posn_check(s) and symbol_check(s)

def min_letter_check(s):
    i = 0
    for c in s:
        if c.isalpha():
            i += 1
            if i == 2:
                return True
    return False


def length_check(s):
    return 2 <= len(s) <= 6

def num_posn_check(s):
    last = len(s) - 1
    while s[last].isnumeric():
        if int(s[last]) == 0 and not(s[last - 1].isnumeric()):
            last += 1
            break
        last -= 1

    for c in s[:last]:
        if c.isnumeric():
            return False
    return True


def symbol_check(s):
    for c in s:
        if not(c.isalnum()):
            return False
    return True

if __name__ == "__main__":
    main()
