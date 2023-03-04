cities = {}

for i in range(10000):
    command = input()
    if command == "Sail":
        break

    city, population, gold = command.split("||")
    population = int(population)
    gold = int(gold)

    if city not in cities:
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold

for i in range(10000):
    text = input()
    if text == "End":
        break

    event = text.split("=>")

    if event[0] == "Plunder":
        town = event[1]
        people = int(event[2])
        gold = int(event[3])
        cities[town][0] -= people
        cities[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")

    elif event[0] == "Prosper":
        town = event[1]
        gold = int(event[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        elif gold >= 0:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

if len(cities):
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for current_city, people_gold in cities.items():
        print(current_city, "->", "Population:", people_gold[0], "citizens,", "Gold:", people_gold[1], "kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")