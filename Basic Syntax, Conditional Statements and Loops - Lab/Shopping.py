b = int(input())
c = input()

while c != "End":
    p_p = int(c)
    b -= p_p
    if b < 0:
        print("You went in overdraft!")
        break
    c = input()
else:
    print("You bought everything needed.")