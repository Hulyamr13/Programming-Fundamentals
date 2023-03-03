n = int(input())
l_n = 0
n_list = []
for i in str(n):
    digit = int(i)
    n_list.append(digit)
num_list_final = sorted(n_list, reverse=True)
print(*num_list_final, sep="")