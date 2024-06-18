def find_min_max(numbers_list):
    return min(numbers_list), max(numbers_list)

numbers = [40, 10, 20, 30, 50]
min_value, max_value = find_min_max(numbers)
print(f"The minimum value is {min_value} and the maximum value is {max_value}.")
