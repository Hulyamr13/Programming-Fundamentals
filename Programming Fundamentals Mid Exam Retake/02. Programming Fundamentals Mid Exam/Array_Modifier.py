array = input().split()

while True:
    command = input().split()
    if command[0] == "end":
        break

    if command[0] == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        array[index1], array[index2] = array[index2], array[index1]

    elif command[0] == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        array[index1] = int(array[index1]) * int(array[index2])

    elif command[0] == "decrease":
        array = [int(x) - 1 for x in array]

print(", ".join(str(x) for x in array))