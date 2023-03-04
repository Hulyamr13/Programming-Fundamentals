def modify_array(arr, command):
    command_parts = command.split()
    if command_parts[0] == "swap":
        index1, index2 = map(int, command_parts[1:])
        arr[index1], arr[index2] = arr[index2], arr[index1]
    elif command_parts[0] == "multiply":
        index1, index2 = map(int, command_parts[1:])
        arr[index1] *= arr[index2]
    elif command_parts[0] == "decrease":
        arr = [x - 1 for x in arr]
    return arr

# Main program
initial_array = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break
    initial_array = modify_array(initial_array, command)

print(", ".join(str(x) for x in initial_array))