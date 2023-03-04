targets = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "End":
        break

    tokens = command.split()
    action = tokens[0]
    index = int(tokens[1])

    if action == "Shoot":
        power = int(tokens[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif action == "Add":
        value = int(tokens[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        radius = int(tokens[2])
        start_index = index - radius
        end_index = index + radius
        if start_index < 0 or end_index >= len(targets):
            print("Strike missed!")
        else:
            del targets[start_index:end_index + 1]
    else:
        print("Invalid command!")

print("|".join(str(x) for x in targets))