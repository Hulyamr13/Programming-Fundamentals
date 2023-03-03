messages = int(input())
for message in range(messages):
    n = int(input())
    if n == 88:
        print("Hello")
    if n == 86:
        print("How are you?")
    if n != 86 and n < 88:
        print("GREAT!")
    if n > 88:
        print("Bye.")