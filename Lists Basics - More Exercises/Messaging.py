numbers = input().split(" ")
letters = list(input())
indexes = []
final_word = []
for i in range(len(numbers)):
    s = 0
    for digit in numbers[i]:
        s += int(digit)
    indexes.append(s)

for i in range(len(indexes)):
    index = indexes[i]
    try:
        final_word.append(letters[index])
    except IndexError:
        index = (index % len(letters))
        final_word.append(letters[index])
    letters.remove(letters[index])

print("".join(final_word))