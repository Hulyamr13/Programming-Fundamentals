message = input()

while True:
    command = input()
    if command == "Reveal":
        break

    action, *params = command.split(":|:")

    if action == "InsertSpace":
        index = int(params[0])
        message = message[:index] + " " + message[index:]

    elif action == "Reverse":
        substring = params[0]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
        else:
            print("error")
            continue

    elif action == "ChangeAll":
        substring, replacement = params
        message = message.replace(substring, replacement)

    print(message)

print(f"You have a new text message: {message}")