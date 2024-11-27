def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

data = [64, 34, 25, 12, 22, 11, 90]
target = 25
print("Linear Search Index:", linear_search(data, target))
