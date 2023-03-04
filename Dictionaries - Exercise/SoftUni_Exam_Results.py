def exam_results(students_dict, submissions):
    print("Results:")
    for key, value in students_dict.items():
        print(f"{key} | {value[1]}")
    print("Submissions:")
    for key, value in submissions.items():
        print(f"{key} - {value}")


def main():
    students_dict = {}
    submissions = {}
    command = input().split("-")
    while command[0] != "exam finished":
        person = command[0]
        if command[1] == "banned":
            if person in students_dict:
                del students_dict[person]
            command = input().split("-")
            continue

        language = command[1]
        points = int(command[2])

        if person not in students_dict:
            students_dict[person] = {language: points}
        elif language not in students_dict[person]:
            students_dict[person][language] = points
        else:
            students_dict[person][language] = max(students_dict[person][language], points)

        if language in submissions:
            submissions[language] += 1
        else:
            submissions[language] = 1

        command = input().split("-")

    # Convert the student's dictionary to the required format for exam_results function
    students = {}
    for key, value in students_dict.items():
        max_points = max(value.values())
        students[key] = [list(value.keys())[list(value.values()).index(max_points)], max_points]

    exam_results(students, submissions)


main()