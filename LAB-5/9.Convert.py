def create_new_list_from_tuple(tup, indices, string_value):
    new_list = [tup[i] for i in indices if i < len(tup)] 
    int_value = int(string_value)
    new_list.append(int_value)
    return new_list

tuple_input = input("Enter the elements of the tuple: ")
tuple_elements = tuple(map(int, tuple_input.split()))

indices_input = input("Enter the indices of elements to take from the tuple: ")
indices = list(map(int, indices_input.split()))

string_value_input = input("Enter a string value to convert to an integer: ")
result_list = create_new_list_from_tuple(tuple_elements, indices, string_value_input)

print("New list:", result_list)
