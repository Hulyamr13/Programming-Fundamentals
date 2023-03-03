def absolute(values):
    final_values = []
    for i in values:
        num = float(i)
        final_values.append(abs(num))
    print(final_values)

input = input().split(' ')
absolute(input)