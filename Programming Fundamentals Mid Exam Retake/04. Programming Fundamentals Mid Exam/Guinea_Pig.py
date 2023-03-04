# Initialize initial values
food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000

# Loop over each day for a month (30 days)
for day in range(1, 31):
    # Give the puppy 300 grams of food each day
    food -= 300

    # Give the puppy hay every second day equal to 5% of the remaining food
    if day % 2 == 0:
        hay_needed = int(food * 0.05)
        hay -= hay_needed

    # Cover the puppy every third day with a quantity of 1/3 of its weight
    if day % 3 == 0:
        cover_needed = int(weight / 3)
        cover -= cover_needed

    # If any of the supplies become negative, print an error message and break the loop
    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        break

# If the loop completes without breaking, all supplies are sufficient
else:
    # Calculate the excess food, hay, and cover and print the result
    excess_food = food / 1000
    excess_hay = hay / 1000
    excess_cover = cover / 1000
    print(f"Everything is fine! Puppy is happy! Food: {excess_food:.2f}, Hay: {excess_hay:.2f}, Cover: {excess_cover:.2f}.")
