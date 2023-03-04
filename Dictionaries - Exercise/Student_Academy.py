def get_average_grade(grades):
    return sum(grades) / len(grades)


n = int(input())

grades_by_student = {}

for _ in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in grades_by_student:
        grades_by_student[student_name] = []

    grades_by_student[student_name].append(student_grade)

average_grade_by_student = {student: get_average_grade(grades) for student, grades in grades_by_student.items()
                            if get_average_grade(grades) >= 4.50}

for student, average_grade in average_grade_by_student.items():
    print(f"{student} -> {average_grade:.2f}")