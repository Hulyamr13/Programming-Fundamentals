people = int(input())
lift = list(map(int, input().split()))
total_spaces = len(lift) * 4
occupied_spaces = sum(lift)

while people > 0 and occupied_spaces < total_spaces:
    for i in range(len(lift)):
        while lift[i] < 4 and people > 0:
            lift[i] += 1
            people -= 1
            occupied_spaces += 1
            if people == 0 or occupied_spaces == total_spaces:
                break
    if people == 0 or occupied_spaces == total_spaces:
        break

if people == 0 and occupied_spaces < total_spaces:
    print("The lift has empty spots!")
    print(*lift)
elif people > 0 and occupied_spaces == total_spaces:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*lift)
else:
    print(*lift)