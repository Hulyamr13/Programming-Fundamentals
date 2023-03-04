contests = {}
users = {}

# Read contests and passwords
while True:
    line = input()
    if line == "end of contests":
        break
    contest, password = line.split(":")
    contests[contest] = password

# Read submissions and update users' points
while True:
    line = input()
    if line == "end of submissions":
        break
    contest, password, user, points = line.split("=>")
    if contest in contests and contests[contest] == password:
        points = int(points)
        if user not in users:
            users[user] = {}
        if contest not in users[user]:
            users[user][contest] = 0
        if points > users[user][contest]:
            users[user][contest] = points

# Calculate total points for each user
total_points = {}
for user, contests in users.items():
    total_points[user] = sum(contests.values())

# Print best candidate
best_user = max(total_points, key=total_points.get)
print(f"Best candidate is {best_user} with total {total_points[best_user]} points.")
print('Ranking:')

# Print ranking
for user in sorted(users.keys()):
    print(user)
    for contest, points in sorted(users[user].items(), key=lambda x: (-x[1], x[0])):
        print(f"#  {contest} -> {points}")