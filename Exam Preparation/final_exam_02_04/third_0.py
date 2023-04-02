liked_meals = {}
disliked_meals_count = 0

while True:
    command = input()

    if command == "Stop":
        break

    like_dislike, guest, meal = command.split('-')

    if like_dislike == "Like":
        if guest in liked_meals and meal not in liked_meals[guest]:
            liked_meals[guest].append(meal)
        elif guest not in liked_meals:
            liked_meals[guest] = [meal]

    elif like_dislike == "Dislike":
        if guest not in liked_meals:
            print(guest + " is not at the party.")
        elif meal not in liked_meals[guest]:
            print(guest + " doesn't have the " + meal + " in his/her collection.")
        else:
            disliked_meals_count += 1
            liked_meals[guest].remove(meal)
            print(guest + " doesn't like the " + meal + ".")

for guest, meals in liked_meals.items():
    print(guest + ": " + ', '.join(meals))

print("Unliked meals: " + str(disliked_meals_count))