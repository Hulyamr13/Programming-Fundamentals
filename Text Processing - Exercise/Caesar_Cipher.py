def caesar_cipher(string):
    text = ''
    for char in string:
         text += chr(ord(char) + 3)
    return text


character = input()
print(caesar_cipher(character))