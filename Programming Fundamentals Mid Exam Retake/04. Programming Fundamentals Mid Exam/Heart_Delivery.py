neighborhood = list(map(int, input().split("@")))
command = input()

cupid_position = 0

while not command == "Love!":
    jump, length = command.split()
    length = int(length)
    new_position = cupid_position + length

    if new_position >= len(neighborhood):
        new_position = 0

    if neighborhood[new_position] == 0:
        print(f"Place {new_position} already had Valentine's day.")
    else:
        neighborhood[new_position] -= 2
        if neighborhood[new_position] == 0:
            print(f"Place {new_position} has Valentine's day.")

    cupid_position = new_position
    command = input()

print(f"Cupid's last position was {cupid_position}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    not_celebrated_count = len([h for h in neighborhood if h != 0])
    print(f"Cupid has failed {not_celebrated_count} places.")