print("Welcome to Highest Score Finder\n")

student_scores = input("Enter scores separated by space: ").split()

highest_score = 0

for score in student_scores:
    score = int(score)
    if score > highest_score:
        highest_score = score

print(f"The highest score is: {highest_score}")
