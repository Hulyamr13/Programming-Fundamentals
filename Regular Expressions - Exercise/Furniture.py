import re

items = input()

pattern = re.compile(
    r">>(?P<furniture_name>[A-Za-z]+)<<(?P<price>[0-9]+[\.0-9]*)!(?P<quantity>[0-9]+)")

total = 0
print("Bought furniture:")
while items != "Purchase":
    result = re.finditer(pattern, items)
    for show in result:
        total += float(show["price"]) * float(show["quantity"])
        print(show["furniture_name"])
    items = input()

print(f"Total money spend: {total:.2f}")