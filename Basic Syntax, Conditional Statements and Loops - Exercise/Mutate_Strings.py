w1 = input()
w2 = input()
loop = w1
length = len(w1)
for i in range(len(w1)):
    loop = loop[:i] + w2[i] + loop[i + 1:]
    if w1[i] == w2[i]:
        continue
    print(loop)
    if loop == w2:
        break