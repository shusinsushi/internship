def count_occurrences(target_list, element_to_count):
    return target_list.count(element_to_count)

my_list = [1, 2, 3, 4, 2, 2, 5]
element = 2
print(f"The element {element} occurs {count_occurrences(my_list, element)} times in the list.")
