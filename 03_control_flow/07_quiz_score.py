# 7. Quiz Score Grader
# Convert a numeric score (0–100) into a letter grade using chained if/elif.
# Use ranges ≥90, ≥80, ≥70, ≥60, else fail.
# Print both the grade and the type of score, referencing max_score = 100.

print("Welcome to Quizz Score Grader!")
score = int(input("Enter your score (0-100): "))
max_score = 100

if score >= 90:
    print(f"You got 'A', {score/max_score*100:.2f}% Congratulations!")
elif score >= 80:
    print(f"You got 'B', {score/max_score*100:.2f}% Congratulations!")
elif score >= 70:
    print(f"You got 'C', {score/max_score*100:.2f}% Congratulations!")
elif score >= 60:
    print(f"You got 'D', {score/max_score*100:.2f}% You need to work more!")
else:
    print(f"You failed the exam!")
print("Thank you for using the Quiz Score Grader!")
print("------------------------------------------")
print(f"Score data type: {type(score)}")
print(f"Max score data type: {type(max_score)}")