
# Lab 2 - Task 1: String Manipulation Challenge

sentence = input("Enter a sentence: ")

# Convert the sentence to uppercase.
print("Uppercase:", sentence.upper())

# Reverse the sentence.
print("Reversed:", sentence[::-1])

# Count vowels regardless of case.
vowels = "aeiou"
vowel_count = sum(1 for character in sentence.lower() if character in vowels)
print("Vowel Count:", vowel_count)

# Replace every space with a hyphen.
print("Spaces Replaced:", sentence.replace(" ", "-"))
