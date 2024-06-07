def main():
    expression = input("Enter: ")
    x, y, z = expression.split(" ")

    match y:
        case "+":
            print(f"{int(x) + int(z) : .1f}")
        case "-":
            print(f"{int(x) - int(z) : .1f}")
        case "/":
            print(f"{int(x) / int(z) : .1f}")
        case "*":
            print(f"{int(x) * int(z) : .1f}")

main()
