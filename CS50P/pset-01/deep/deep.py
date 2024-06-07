def main():
    ans = input("What is your answer to the Great Question of Life, the Universe and Everything? ")
    if ans_found(ans):
        print("Yes")
    else:
        print("No")

def ans_found(a):
    if a.find("42") != -1 or a.lower().find("forty-two") != -1 or a.lower().find("forty two") != -1:
        return True
    return False

main()
