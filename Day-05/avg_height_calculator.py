print("Welcome to Average Height Calculator\n")

student_heights = input("Enter heights separated by space: ").split()

total_height = 0
number_of_students = 0

for height in student_heights:
    total_height += int(height)
    number_of_students += 1

average_height = round(total_height / number_of_students)

print(f"Total Height = {total_height}")
print(f"Number of Students = {number_of_students}")
print(f"Average Height = {average_height}")
