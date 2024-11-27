def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

data = [64, 34, 25, 12, 22, 11, 90]
print("Selection Sorted:", selection_sort(data))
