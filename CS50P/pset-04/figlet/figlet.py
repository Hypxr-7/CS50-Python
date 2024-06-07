from pyfiglet import Figlet
import sys
import random

def main():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid Number of Arguments")


    figlet = Figlet()


    if len(sys.argv) == 3:
        if (sys.argv[1] != "-f" and sys.argv[1] != "--font") or (sys.argv[2] not in figlet.getFonts()):
            sys.exit("Invalid Arguments")


    if (len(sys.argv) == 1):
        figlet.setFont(font=random.choice(figlet.getFonts()))
    else:
        figlet.setFont(font=sys.argv[2])


    response = input("Enter: ")
    print(figlet.renderText(response))



if __name__ == "__main__":
    main()
