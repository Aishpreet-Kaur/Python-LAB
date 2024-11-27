def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

data = [64, 34, 25, 12, 22, 11, 90]
print("Insertion Sorted:", insertion_sort(data))
