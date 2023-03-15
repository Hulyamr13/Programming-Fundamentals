words = input().split()
first_word = words[0]
second_word = words[1]

min_len = min(len(first_word), len(second_word))
result = 0
for idx in range(min_len):
    first_word_char = first_word[idx]
    second_word_char = second_word[idx]
    result += ord(first_word_char) * ord(second_word_char)

result += sum([ord(char) for char in first_word[min_len:]])
result += sum([ord(char) for char in second_word[min_len:]])

print(result)