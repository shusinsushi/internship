import string

def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

your_string = "Hello, world! How are you?"
clean_string = remove_punctuation(your_string)
print(clean_string)
