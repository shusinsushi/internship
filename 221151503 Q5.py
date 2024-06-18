user_input = input("Please enter some text: ")

with open('user_input.txt', 'w') as file:
    file.write(user_input)

print("Your input has been written to 'user_input.txt'")
