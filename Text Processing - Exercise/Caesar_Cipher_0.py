text = input()

encrypted_text = ''
for ch in text:
    new_ascii_value = ord(ch) + 3
    encrypted_text += chr(new_ascii_value)

print(encrypted_text)


encrypted_text = ''.join([chr(ord(ch) + 3) for ch in text])
print(encrypted_text)