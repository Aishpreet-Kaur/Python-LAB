def convert_to_strings(int_list, int_tuple):
    list_strings = list(map(str, int_list))
    tuple_strings = list(map(str, int_tuple))
    
    return list_strings, tuple_strings

list_input = input("Enter a list of integers, separated by spaces: ")
int_list = list(map(int, list_input.split()))

tuple_input = input("Enter a tuple of integers, separated by spaces: ")
int_tuple = tuple(map(int, tuple_input.split()))

list_strings, tuple_strings = convert_to_strings(int_list, int_tuple)

print("List of strings:", list_strings)
print("Tuple of strings (as a list):", tuple_strings)
