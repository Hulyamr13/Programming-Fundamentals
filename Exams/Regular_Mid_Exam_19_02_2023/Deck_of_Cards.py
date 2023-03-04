cards = input().split(", ")
n = int(input())

for i in range(n):
    command = input().split(", ")
    if command[0] == "Add":
        if command[1] in cards:
            print("Card is already in the deck")
        else:
            cards.append(command[1])
            print("Card successfully added")
    elif command[0] == "Remove":
        if command[1] in cards:
            cards.remove(command[1])
            print("Card successfully removed")
        else:
            print("Card not found")
    elif command[0] == "Remove At":
        index = int(command[1])
        if index < 0 or index >= len(cards):
            print("Index out of range")
        else:
            cards.pop(index)
            print("Card successfully removed")
    elif command[0] == "Insert":
        index = int(command[1])
        card = command[2]
        if index < 0 or index >= len(cards):
            print("Index out of range")
        elif card in cards:
            print("Card is already added")
        else:
            cards.insert(index, card)
            print("Card successfully added")

print(", ".join(cards))