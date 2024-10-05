def compute_sum(int_array):
    integer_elements = list(map(int, int_array))
    total_sum = sum(integer_elements)
    return total_sum

array_input = input("Enter the elements of the array, separated by spaces: ")
int_array = array_input.split()
result = compute_sum(int_array)
print("The sum of the elements in the array is:", result)
