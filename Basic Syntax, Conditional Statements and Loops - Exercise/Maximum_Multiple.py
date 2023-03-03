div = int(input())
m_n = int(input())

for num in range(m_n, 0, -1):
    if num % div == 0:
        print(num)
        break