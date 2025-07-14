# 7. Grade Letter Converter - Convert numeric grades to letter grades
# Uses loops and conditional logic to process a list of numeric scores
# Demonstrates combining loops with if/elif statements for classification
# Shows practical application of grade conversion systems

# Project Instructions:
# Convert a list of numeric grades (0-100) to letter grades
# Use loops to process each score and conditional logic for conversion
# Standard grading scale:
# - A: 90-100
# - B: 80-89
# - C: 70-79
# - D: 60-69
# - F: 0-59

# Example scores:
# scores = [95, 87, 72, 65, 58, 91, 83, 77, 69, 94]

# Expected output:
# Score 95 → Grade A
# Score 87 → Grade B
# Score 72 → Grade C
# etc.

# Bonus challenges:
# - Calculate class average
# - Count how many of each letter grade
# - Add plus/minus grades (A-, B+, etc.)
# - Show grade distribution statistics

# TODO: Implement your solution here

print("Welcome to the Grade Letter Converter!")
print("This program will convert numeric grades to letter grades based on standard grading scales.")
scores = [95, 87, 72, 65, 58, 91, 83, 77, 69, 94, 45]
grades = []

for score in scores:
    if score >= 90:
        print(f"Score {score} → Grade: A")
        grades.append('A')
    elif score >= 80:
        print(f"Score {score} → Grade: B")
        grades.append('B')
    elif score >= 70:
        print(f"Score {score} → Grade: C")
        grades.append('C')
    elif score >= 60:
        print(f"Score {score} → Grade: D")
        grades.append('D')
    else:
        print(f"Score {score} → Grade: F")
        grades.append('F')      


count_scores = len(scores)
sum = 0
for score in scores:
    sum += score

average = sum / count_scores
print(f"\n📊 CLASS PERFORMANCE ANALYSIS 📊")
print(f"\n🎯  Class Average: {average:.2f} (C+ performance)")
print(f"\n🏆  Excellence (A): {grades.count('A')} students achieved top marks!")
print(f"\n👍  Good Work (B): {grades.count('B')} students in the B")
print(f"\n📈  Satisfactory (C): {grades.count('C')} students meeting standards")
print(f"\n⚠️  Needs Improvement (D): {grades.count('D')} students need support")
print(f"\n🔴 Requires Attention (F): {grades.count('F')} students need help\n")

