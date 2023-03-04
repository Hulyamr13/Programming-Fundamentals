numbers = list(map(int, input().split()))
average = sum(numbers) / len(numbers)
top_numbers = sorted(filter(lambda x: x > average, numbers), reverse=True)[:5]

if top_numbers:
    print(' '.join(map(str, top_numbers)))
else:
    print('No')