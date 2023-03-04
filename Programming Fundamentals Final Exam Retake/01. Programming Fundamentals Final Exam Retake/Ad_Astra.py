import re

string = input()
pattern = r"([|#])(\w+(\s\w+|\S))\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
food = re.findall(pattern, string)

needed_calories_per_day = 2000
total_calories = sum(int(element[-1]) for element in food)
days_to_last = total_calories // needed_calories_per_day

print(f"You have food to last you for: {days_to_last} days!")

i = 0
while i < len(food):
    item = food[i][1]
    date = food[i][3]
    calories = food[i][4]
    print(f"Item: {item}, Best before: {date}, Nutrition: {calories}")
    i += 1