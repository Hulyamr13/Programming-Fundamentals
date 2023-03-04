col = int(input())
board = []
att = []
count = 0


for i in range(col):
    rows = input().split(" ")
    board.append([rows])

attacks = input().split(" ")
while True:
    for i, j in enumerate(attacks):
        att.append([])
        for o in j:
            if o.isdigit():
                att[i].append(int(o))
    while len(att) > 0:
        for i, j in enumerate(board):
            if len(att) == 0:
                break
            if att[0][0] <= col:
                if i == att[0][0]:
                    if j[0][att[0][-1]] == "0":
                        att.pop(0)
                    else:
                        if j[0][att[0][-1]] == "1":
                            count += 1
                            j[0][att[0][-1]] = "0"
                            att.pop(0)
                        else:
                            j[0][att[0][-1]] = str(int(j[0][att[0][-1]]) - 1)
                            att.pop(0)
    break
print(count)