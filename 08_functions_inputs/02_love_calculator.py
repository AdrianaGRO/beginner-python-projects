"""
Love Calculator

Task:
Create a function called calculate_love_score() that tests the compatibility between two names using the letters in "TRUE" and "LOVE".
- The function should take two names as arguments.
- Count the occurrences of T, R, U, E in both names (case-insensitive).
- Count the occurrences of L, O, V, E in both names.
- Combine the two totals to form a two-digit score (e.g., TRUE total = 5, LOVE total = 3, score = 53).
- Print the score in the format:
  Love score for X and Y is Z
  (where X and Y are the names, Z is the score)

Example:
If you call calculate_love_score("Kanye West", "Kim Kardashian"), the output should be:
Love score for Kanye West and Kim Kardashian is 42

Note:
For testing, use hard-coded values instead of input().
"""


def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()


    true_count = 0
    for letter in "true":
        true_count += combined_names.count(letter)
    love_count = 0
    for letter in "love":
        love_count += combined_names.count(letter)

    score = int(f"{true_count}{love_count}")
    print(f"Love score for {name1} and {name2} is {score}")

calculate_love_score("Kanye West", "Kim Kardashian")  # Output: 42


def calculate_love_score_course(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score_course("Kanye West", "Kim Kardashian")