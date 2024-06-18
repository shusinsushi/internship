def read_lines():
    lines = []
    print("Enter multiple lines of text. Enter an empty line to finish.")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines

lines = read_lines()
print("\nYou entered:")
for line in lines:
    print(line)
