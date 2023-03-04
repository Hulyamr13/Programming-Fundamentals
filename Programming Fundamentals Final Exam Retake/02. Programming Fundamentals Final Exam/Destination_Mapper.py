import re

pattern = r"([\/=])([A-Z][a-zA-z]{2,})\1"
places = input()

valid_places = []
matches = re.finditer(pattern, places)

while True:
    try:
        current_match = next(matches)
        current_place = current_match.group(2)
        valid_places.append(current_place)
    except StopIteration:
        break

travel_points = sum(len(place) for place in valid_places)

print(f"Destinations: {', '.join(valid_places)}")
print(f"Travel Points: {travel_points}")