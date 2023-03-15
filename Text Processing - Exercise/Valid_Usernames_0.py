from string import ascii_letters, digits

usernames = input().split(", ")
allowed_chars = ascii_letters + digits + "-" + "_"

for username in usernames:
    if len(username) < 3 or len(username) > 16:
        continue

    temp = [char in allowed_chars for char in username]
    contains_allowed_char = all(temp)
    if not contains_allowed_char:
        continue

    print(username)