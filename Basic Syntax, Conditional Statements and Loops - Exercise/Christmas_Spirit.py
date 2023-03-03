ornament = [2, 5]
skirt = [5, 3]
garland = [3, 10]
lights = [15, 17]
quantity = int(input())
days = int(input())
total_price = 0
total_spirit = 0
for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_price += ornament[0] * quantity
        total_spirit += ornament[1]
    if day % 3 == 0:
        total_price += (garland[0] + skirt[0]) * quantity
        total_spirit += garland[1] + skirt[1]
    if day % 5 == 0:
        total_price += lights[0] * quantity
        total_spirit += lights[1]
    if day % 5 == 0 and day % 3 == 0:
        total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_price += garland[0] + skirt[0] + lights[0]
    if day % 10 == 0 and day == days:
        total_spirit -= 30
print(f"Total cost: {total_price}")
print(f"Total spirit: {total_spirit}")