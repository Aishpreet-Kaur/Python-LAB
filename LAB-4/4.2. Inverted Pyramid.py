def inverted_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (i - 1) + (f"{i} " * (rows - i + 1)).strip())

inverted_pyramid(5)
