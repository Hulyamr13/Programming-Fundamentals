dwarfs = {}

while True:
    data = input()
    if data == "Once upon a time":
        break
    name, hat_color, physics = data.split(" <:> ")
    physics = int(physics)
    key = (name, hat_color)
    if key not in dwarfs:
        dwarfs[key] = physics
    else:
        dwarfs[key] = max(physics, dwarfs[key])

sorted_dwarfs = sorted(dwarfs.items(), key=lambda x: (-x[1], -sum(1 for y in dwarfs if y[1] == x[0][1])))

for dwarf, physics in sorted_dwarfs:
    print(f"({dwarf[1]}) {dwarf[0]} <-> {physics}")