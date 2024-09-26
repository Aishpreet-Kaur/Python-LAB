def sort_strings(strings):
    return sorted(strings)

mylist = input("Enter a list of words separated by spaces: ")
strings_list = mylist.split()
sorted_list = sort_strings(strings_list)
print("Sorted strings:", sorted_list)
