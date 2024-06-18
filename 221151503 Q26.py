def check_string(s, prefix, suffix):
    return s.startswith(prefix) or s.endswith(suffix)

my_string = "hello world"
print(check_string(my_string, "he", "ld"))  # Output: True
print(check_string(my_string, "world", "lo"))  # Output: False
