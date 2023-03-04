words = input().split()

result = []

for word in words:
    if len(word) % 2 == 0:
        result.append(word)

print('\n'.join(result))