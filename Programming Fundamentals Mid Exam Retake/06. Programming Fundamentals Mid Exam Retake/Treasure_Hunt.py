loot = input().split("|")
command = input()
stolen_items = []

while command != "Yohoho!":
    tokens = command.split()
    if tokens[0] == "Loot":
        for item in tokens[1:]:
            if item not in loot:
                loot.insert(0, item)
    elif tokens[0] == "Drop":
        index = int(tokens[1])
        if 0 <= index < len(loot):
            loot.append(loot.pop(index))
    elif tokens[0] == "Steal":
        count = int(tokens[1])
        stolen_items = loot[-count:]
        loot = loot[:-count]
        stolen_items.reverse()
        print(", ".join(reversed(stolen_items)))
    command = input()

if len(loot) == 0:
    print("Failed treasure hunt.")
else:
    total_length = sum([len(item) for item in loot])
    average_gain = total_length / len(loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")