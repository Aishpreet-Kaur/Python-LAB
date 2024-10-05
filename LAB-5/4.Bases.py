def power_list(bases):
    return list(map(lambda x: bases[x] ** x, range(len(bases))))

bases_input = input("Enter the bases, separated by spaces: ")

bases = list(map(int, bases_input.split()))

result = power_list(bases)
print("The result is:", result)
