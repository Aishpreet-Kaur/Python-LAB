levels = 4
current_number = 1

for i in range(1, levels + 1):
    last_number = current_number + i - 1
    for j in range(last_number, current_number - 1, -1):
        print(j, end=" ")
    current_number += i
    print()
