def convert_and_remove_duplicates():
    sequence = input("Enter a sequence: ")
    unique_chars = ''.join(sorted(set(sequence), key=sequence.index))

    uppercase_sequence = list(map(str.upper, unique_chars))
    lowercase_sequence = list(map(str.lower, unique_chars))

    print("Uppercase sequence without duplicates:", ''.join(uppercase_sequence))
    print("Lowercase sequence without duplicates:", ''.join(lowercase_sequence))

convert_and_remove_duplicates()
