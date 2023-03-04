elements = {}
word = input().lower().split()
odd_occurrences = []

for i in word:
    if i in elements:
        elements[i] += 1
    else:
        elements[i] = 1

for i in elements.keys():
    if elements.get(i) % 2 != 0 and i not in odd_occurrences:
        odd_occurrences.append(i)

print(" ".join(odd_occurrences))