vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U')
text = input()
for char in text:

    if char in vowels:

        text = text.replace(char, '')

print(text)