groceries = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    command_tokens = command.split()
    action = command_tokens[0]
    item = command_tokens[1]

    if action == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)

    elif action == "Unnecessary":
        if item in groceries:
            groceries.remove(item)

    elif action == "Correct":
        new_item = command_tokens[2]
        if item in groceries:
            index = groceries.index(item)
            groceries[index] = new_item

    elif action == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

print(", ".join(groceries))