# 6. Quiz Question Picker - Random quiz game with score tracking
# Uses random selection to pick questions from a list without repetition
# Manages parallel lists for questions and answers using index tracking
# Keeps score and provides final results based on user performance
import random

# Project Instructions:
# 1. Build a list of question strings (and a parallel list of answers)
# 2. Ask the user how many questions they'd like
# 3. For each turn, randomly select an unused index, present the question, and check the answer
# 4. Keep score and display the final result

# Extended list of question strings
questions = [
    "What is the capital of France?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the square root of 64?",
    "What is the chemical symbol for water?",
    "Who painted the Mona Lisa?",
    "What planet is known as the Red Planet?",
    "In which year did World War II end?",
    "What is the largest mammal in the world?",
    "Who developed the theory of relativity?",
    "What is the currency of Japan?",
    "Which element has the atomic number 1?",
    "How many continents are there on Earth?",
    "Who is known as the father of computers?",
    "Which language is primarily spoken in Brazil?",
    "What gas do plants absorb from the atmosphere?"
]

# Corresponding extended list of answers
answers = [
    "Paris",
    "Harper Lee",
    "8",
    "H2O",
    "Leonardo da Vinci",
    "Mars",
    "1945",
    "Blue whale",
    "Albert Einstein",
    "Yen",
    "Hydrogen",
    "7",
    "Charles Babbage",
    "Portuguese",
    "Carbon dioxide"
]


print("===Welcome to Quiz Question Picker===")
user_num_question= int(input("How many questions you would like to have (choose form  1- 10): \n"))
print(f"You choose a set of {user_num_question}. Let's do this...")
available_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
score = 0

if user_num_question >= 1:
    random_index = random.choice(available_indices) # Choose a random question that hasn't been used
    available_indices.remove(random_index)  # Remove the used index
    answer = answers[random_index] #This grabs the correct answer from the answers list at that same index.

    print(f"Question: {questions[random_index]}") #Get the question using the random index
    answer_user = input("Your answer: ") #Take the answer from the user
    if answer_user.lower() == answer.lower():  # Compare the user's answer to the correct answer
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! the answer was... {answer}")

if user_num_question >= 2:
    random_index = random.choice(available_indices)
    available_indices.remove(random_index)  # Remove the used index
    answer = answers[random_index]
    print(f"Question: {questions[random_index]}")
    answer_user = input("Your answer: ")
    if answer_user.lower() == answer.lower():  # Compare the user's answer to the correct answer
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! the answer was... {answer}")

if user_num_question >= 3:
    random_index = random.choice(available_indices)
    available_indices.remove(random_index)  # Remove the used index
    answer = answers[random_index]
    print(f"Question: {questions[random_index]}")
    answer_user = input("Your answer: ")
    if answer_user.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! the answer was... {answer}")

if user_num_question >= 4:
    random_index = random.choice(available_indices)
    available_indices.remove(random_index)  # Remove the used index
    answer = answers[random_index]
    print(f"Question: {questions[random_index]}")
    answer_user = input("Your answer: ")
    if answer_user.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! the answer was... {answer}")

if user_num_question >= 5:
    random_index = random.choice(available_indices)
    available_indices.remove(random_index)  # Remove the used index
    answer = answers[random_index]
    print(f"Question: {questions[random_index]}")
    answer_user = input("Your answer: ")
    if answer_user.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! the answer was... {answer}")

if user_num_question >= 6:
    random_index = random.choice(available_indices)
    available_indices.remove(random_index)  # Remove the used index
    answer = answers[random_index]
    print(f"Question: {questions[random_index]}")
    answer_user = input("Your answer: ")
    if answer_user.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! the answer was... {answer}")

if user_num_question >= 7:
    random_index = random.choice(available_indices)
    available_indices.remove(random_index)  # Remove the used index
    answer = answers[random_index]
    print(f"Question: {questions[random_index]}")
    answer_user = input("Your answer: ")
    if answer_user.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! the answer was... {answer}")

if user_num_question >= 8:
    random_index = random.choice(available_indices)
    available_indices.remove(random_index)  # Remove the used index
    answer = answers[random_index]
    print(f"Question: {questions[random_index]}")
    answer_user = input("Your answer: ")
    if answer_user.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! the answer was... {answer}")

if user_num_question >= 9:
    random_index = random.choice(available_indices)
    available_indices.remove(random_index)  # Remove the used index
    answer = answers[random_index]
    print(f"Question: {questions[random_index]}")
    answer_user = input("Your answer: ")
    if answer_user.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! the answer was... {answer}")

if user_num_question >= 10:
    random_index = random.choice(available_indices)
    available_indices.remove(random_index)  # Remove the used index
    answer = answers[random_index]
    print(f"Question: {questions[random_index]}")
    answer_user = input("Your answer: ")
    if answer_user.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! the answer was... {answer}")
if user_num_question > 10:
    print("You can only choose up to 10 questions. Please try again.")  
if user_num_question < 1:
    print("You must choose at least 1 question. Please try again.")


print(f"The final score is {score} out of {user_num_question}")

if score == user_num_question:
    print("Perfect score! Excellent work")
elif score >= user_num_question * 0.8:
    print("Great job! You did really well!")
elif score >= user_num_question * 0.6:
    print("Good effort! Keep practicing!")
else:
    print("Keep studying and try again")