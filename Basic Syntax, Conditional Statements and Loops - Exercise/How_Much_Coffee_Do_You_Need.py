coffee = 0
while True:
    events = input()
    if events == "END":
        break
    if events.lower() == "cat" or events.lower() == "coding" or events.lower() == "dog" or events.lower() == "movie":
        if events.isupper():
            coffee += 2
        else:
            coffee += 1
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)