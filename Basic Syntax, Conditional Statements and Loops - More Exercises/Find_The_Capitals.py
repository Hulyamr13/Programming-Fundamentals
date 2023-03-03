word = input()
w_l = []
capital = []

for c in word:
    w_l.append(c)

for i in range(len(w_l)):
    letter = w_l[i]
    if letter.isupper():
        capital.append(i)

print(capital)