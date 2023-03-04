count_plants = int(input())
all_plants = {}

for _ in range(count_plants):
    input_split = input().split("<->")
    if len(input_split) == 2:
        plant, rarity = input_split
        all_plants[plant] = {'rarity': int(rarity), 'rating': []}
    else:
        print("error")
        continue

command = input()

while command != "Exhibition":
    command = command.split()
    action = command[0]
    current_plant = command[1]

    if current_plant not in all_plants:
        print("error")
        command = input()
        continue

    if action == "Rate:":
        rating = int(command[3])
        all_plants[current_plant]['rating'].append(rating)
    elif action == "Update:":
        new_rarity = int(command[3])
        all_plants[current_plant]['rarity'] = new_rarity
    elif action == "Reset:":
        all_plants[current_plant]['rating'] = []

    command = input()

print("Plants for the exhibition:")
for plant, info in all_plants.items():
    rarity = info['rarity']
    rating = 0
    if len(info['rating']):
        rating = sum(info['rating']) / len(info['rating'])
    print(f"- {plant}; Rarity: {rarity}; Rating: {rating:.2f}")