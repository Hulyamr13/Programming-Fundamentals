activation_key = input()

while True:
    command = input()
    if command == "Generate":
        break

    tokens = command.split(">>>")
    action = tokens[0]

    if action == "Contains":
        substring = tokens[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        case = tokens[1]
        start_index = int(tokens[2])
        end_index = int(tokens[3])

        if case == "Upper":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() \
                             + activation_key[end_index:]
        elif case == "Lower":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() \
                             + activation_key[end_index:]

        print(activation_key)

    elif action == "Slice":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f"Your activation key is: {activation_key}")