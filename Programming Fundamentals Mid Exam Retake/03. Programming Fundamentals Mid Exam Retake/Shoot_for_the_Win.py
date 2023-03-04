targets = list(map(int, input().split()))
count_shot = 0

while True:
    command = input()
    if command == "End":
        break

    index = int(command)
    if 0 <= index < len(targets) and targets[index] != -1:
        current_target = targets[index]
        targets[index] = -1
        count_shot += 1

        for i in range(len(targets)):
            if targets[i] == -1:
                continue

            if targets[i] > current_target:
                targets[i] -= current_target
            elif targets[i] <= current_target:
                targets[i] += current_target

print(f"Shot targets: {count_shot} -> {' '.join(map(str, targets))}")