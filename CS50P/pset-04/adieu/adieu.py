import inflect

def main():
    p = inflect.engine()
    word_list = []
    while True:
        try:
            word = input("Enter: ")
            word_list.append(word)
        except EOFError:
            print()
            print("Adieu, adieu, to", p.join(word_list))
            break




if __name__ == "__main__":
    main()
