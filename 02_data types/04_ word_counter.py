# 4. Word Counter
# Develop a program that counts characters and words in a sentence.
# Prompt the user to enter a sentence.
# Calculate and print the total number of characters (including spaces) and the number of words (split by spaces).
# Print the data type of the input sentence.

print("Welcome to the word counter!")
sentence = input("Please enter a sentence:\n")
words = sentence.split()
print(f"The phrase contains: {len(sentence)} - characters")
print(f"The phrase contains: {len(words)} - words")
print(f"Data type of input is: {type(sentence)}")