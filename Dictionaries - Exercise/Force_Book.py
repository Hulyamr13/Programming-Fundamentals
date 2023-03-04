def sides(side_, user_):
    for key in force_book:
        if user_ in force_book[key]:
            return
    force_book[side_] = force_book.get(side_, {})
    force_book[side_][user_] = force_book.get(side_)


def change_side(user_, side_):
    for key in force_book:
        if user_ in force_book[key]:
            del force_book[key][user_]
            break
    force_book[side_] = force_book.get(side_, {})
    force_book[side_][user_] = force_book.get(side_)
    print(f"{user_} joins the {side_} side!")


force_command = input()
force_book = {}

while force_command != "Lumpawaroo":

    if " | " in force_command:
        force_command = force_command.split(" | ")
        sides(str(force_command[0]), str(force_command[-1]))
    elif " -> " in force_command:
        force_command = force_command.split(" -> ")
        change_side(str(force_command[0]), str(force_command[-1]))
    force_command = input()

for side in force_book:
    if force_book[side]:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for name in force_book[side]:
            print(f"! {name}")