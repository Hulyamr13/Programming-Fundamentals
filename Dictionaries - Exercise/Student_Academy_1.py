n = int(input())

grades_by_student = {}

for _ in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in grades_by_student:
        grades_by_student[student_name] = []

    grades_by_student[student_name].append(student_grade)

for student, grades in grades_by_student.items():
    average_grade = sum(grades) / len(grades)
    if average_grade < 4.50:
        continue
    print(f"{student} -> {average_grade:.2f}")