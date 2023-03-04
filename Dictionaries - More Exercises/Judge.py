command = input()

students_dictionary = {"user": {}, "contest": {}}
user_d = "user"
contest_d = "contest"

while command != "no more time":
    user_name, contest, points = command.split(" -> ")
    points = int(points)
    students_dictionary[contest_d].setdefault(contest, {})
    students_dictionary[contest_d][contest].setdefault(user_name, 0)
    students_dictionary[user_d].setdefault(user_name, 0)

    if students_dictionary[user_d].get(user_name) == points:
        students_dictionary[user_d][user_name] += points

    if students_dictionary[contest_d][contest][user_name] < points:
        students_dictionary[user_d][user_name] += points - students_dictionary[contest_d][contest][user_name]
        students_dictionary[contest_d][contest][user_name] = points

    command = input()


def show_result():
    [print(f"{contest}: {len(students_dictionary[contest_d][contest])} participants\n" +
           '\n'.join(f"{i+1}. {k} <::> {v}" for i, (k, v) in enumerate(
               sorted(students_dictionary[contest_d][contest].items(), key=lambda x: (-x[1], x[0])))))
     for contest in students_dictionary[contest_d]]
    print("Individual standings:")
    print('\n'.join(f"{i+1}. {k} -> {v}" for i, (k, v) in enumerate(
        sorted(students_dictionary[user_d].items(), key=lambda x: (-x[1], x[0])))))


show_result()