import sys
readline = sys.stdin.readline

n = int(readline())
customers = []
for I in range(n):
    customers.append(list(map(int, readline().split())))
customers.sort()


ans = 0
interest = 0
for k in range(n):
    temp_i = 0
    for x in customers:
        if x[0] >= customers[k][0]:
            temp = (customers[k][0] - x[1])
            if temp > 0:
                temp_i += temp
    if temp_i > interest:
        ans = customers[k][0]
        interest = temp_i
print(ans)