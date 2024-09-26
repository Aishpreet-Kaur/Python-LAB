def count_vowels(s):
    vowels = "aeiouAEIOU" 
    count = 0
    
    for char in s:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)
print("Number of vowels in the string:", vowel_count)
