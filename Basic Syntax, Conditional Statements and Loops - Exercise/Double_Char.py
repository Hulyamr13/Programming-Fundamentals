while True:
    line = input()
    if line == 'End':
        break
    if line == 'SoftUni':
        continue

    converted_line = ''
    for ch in line:
        converted_line += 2 * ch
    print(converted_line)