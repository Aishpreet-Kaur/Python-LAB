def binary_search(data, target):
    low, high = 0, len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


data = sorted([64, 34, 25, 12, 22, 11, 90])
target = 25
print("Binary Search Index:", binary_search(data, target))
