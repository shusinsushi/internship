def count_character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

your_string = "sample string"
frequency = count_character_frequency(your_string)
for char, freq in frequency.items():
    print(f"'{char}': {freq}")
