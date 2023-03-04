initial_energy = int(input())
distance = input()
won_battles = 0

while distance != "End of battle":
    distance = int(distance)

    if initial_energy < distance:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        break

    initial_energy -= distance
    won_battles += 1

    if won_battles % 3 == 0:
        initial_energy += won_battles

    distance = input()

if distance == "End of battle":
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")