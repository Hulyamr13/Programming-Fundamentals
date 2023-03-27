import re

# read the input string
food_string = input()

# pattern to match the food information
pattern = r'(\||#)([a-zA-Z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'

# match all occurrences of the pattern in the input string
matches = re.findall(pattern, food_string)

# calculate the total calories
total_calories = sum(int(match[3]) for match in matches)

# calculate the number of days of food supply
days_of_supply = total_calories // 2000

# print the number of days of food supply
print(f'You have food to last you for: {days_of_supply} days!')

# print the food information for each item
for match in matches:
    item_name = match[1]
    expiration_date = match[2]
    calories = match[3]
    print(f'Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}')
