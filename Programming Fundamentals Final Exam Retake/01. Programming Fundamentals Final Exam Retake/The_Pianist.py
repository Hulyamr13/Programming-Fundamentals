n = int(input())

pieces = {}
for _ in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = {"composer": composer, "key": key}

while True:
    command = input()
    if command == "Stop":
        break

    tokens = command.split("|")
    action = tokens[0]
    piece = tokens[1]

    if action == "Add":
        composer = tokens[2]
        key = tokens[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        new_key = tokens[2]
        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, info in pieces.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")