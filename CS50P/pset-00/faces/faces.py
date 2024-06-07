def main():
    prompt = input("Enter: ")
    print_faces(prompt)

def print_faces(user_prompt):
    user_prompt = user_prompt.replace(":)", "🙂")
    user_prompt = user_prompt.replace(":(", "🙁")
    print(user_prompt)

main()
