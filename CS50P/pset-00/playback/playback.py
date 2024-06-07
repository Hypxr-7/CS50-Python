def main():
    prompt = input("Enter: ")
    print_playback(prompt)

def print_playback(user_prompt):
    print(user_prompt.replace(" ", "..."))

main()
