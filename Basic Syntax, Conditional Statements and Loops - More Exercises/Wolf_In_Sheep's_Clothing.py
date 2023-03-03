animals = input().split(", ")
WOLF = "wolf"

if animals[-1] == WOLF:
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(animals) - 1, -1, -1):
        if animals[i] == WOLF:
            sheep_position = len(animals) - (abs(i) + 1)
    print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")