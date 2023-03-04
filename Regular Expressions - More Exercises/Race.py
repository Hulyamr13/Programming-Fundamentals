import re

names_of_racers = {name.replace(" ", ""): 0 for name in input().split(",")}
racer_code = input()
name_pattern = re.compile(r"([A-Za-z])")
km_pattern = re.compile(r"([0-9])")
while racer_code != "end of race":
    find_name = "".join(re.findall(name_pattern, racer_code))
    find_numbers = sum(int(num) for num in re.findall(km_pattern, racer_code))
    if find_name in names_of_racers.keys():
        names_of_racers[find_name] += find_numbers
    racer_code = input()

names_of_racers = sorted(names_of_racers.items(), key=lambda x: -x[1])

print(f"1st place: {names_of_racers[0][0]}")
print(f"2nd place: {names_of_racers[1][0]}")
print(f"3rd place: {names_of_racers[2][0]}")