rooms = input().split('|')

health = 100
bitcoins = 0
best_room = 0
dead = False

for best_room, current_room in enumerate(rooms, start=1):
    command, number = current_room.split()
    number = int(number)
    if command == "potion":
        if health + number > 100:
            number = 100 - health
            health = 100
        else:
            health += number
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        if number >= health:
            dead = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            break
        else:
            health -= number
            print(f'You slayed {command}.')

if not dead:
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f"Health: {health}")