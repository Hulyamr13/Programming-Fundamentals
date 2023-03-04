import math

num_students = int(input())
num_lectures = int(input())
bonus = int(input())

max_bonus = 0
max_student_attendances = 0

for i in range(num_students):
    student_attendances = int(input())
    total_bonus = student_attendances / num_lectures * (5 + bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_student_attendances = student_attendances

max_bonus = math.ceil(max_bonus)  # round up to the nearest larger number

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_student_attendances} lectures.")
