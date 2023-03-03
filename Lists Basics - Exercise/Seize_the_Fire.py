High = range(81, 126)
Medium = range(51, 81)
Low = range(1, 51)

fire_data = input().split("#")
water_qty = int(input())

effort = 0
total_fire = 0

fire_type = [i.split(" = ")[0] for i in fire_data]

fire_value = [int(i.split(" = ")[1]) for i in fire_data]

print("Cells:")

for i in range(len(fire_type)):
    if fire_type[i] == "High" and fire_value[i] not in High:
        continue
    elif fire_type[i] == "Medium" and fire_value[i] not in Medium:
        continue
    elif fire_type[i] == "Low" and fire_value[i] not in Low:
        continue
    if fire_value[i] <= water_qty:
        water_qty -= fire_value[i]
        effort += fire_value[i] * 0.25
        total_fire += fire_value[i]
        print(f"- {fire_value[i]}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")