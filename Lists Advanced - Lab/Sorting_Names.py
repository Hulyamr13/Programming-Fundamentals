names = input().split(", ")  # read input and split by comma and space
names.sort(key=lambda x: (-len(x), x))  # sort by length in descending order, then alphabetically in ascending order
print(names)  # print the sorted list
