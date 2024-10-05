def add_and_subtract_lists(list1, list2):
    added_list = list(map(lambda x, y: x + y, list1, list2))
    subtracted_list = list(map(lambda x, y: x - y, list1, list2))
    
    return added_list, subtracted_list

list1_input = input("Enter the first list of numbers, separated by spaces: ")
list2_input = input("Enter the second list of numbers, separated by spaces: ")

list1 = list(map(int, list1_input.split()))
list2 = list(map(int, list2_input.split()))

if len(list1) != len(list2):
    print("Error: Both lists must have the same number of elements.")
else:
    added, subtracted = add_and_subtract_lists(list1, list2)
    print("Added list:", added)
    print("Subtracted list:", subtracted)
