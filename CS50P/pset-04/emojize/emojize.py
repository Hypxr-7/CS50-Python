import emoji

def main():
    emoji_code = input("Enter: ")
    print(emoji.emojize(emoji_code, language="alias"))

if __name__ == "__main__":
    main()
