n, m ,k = map(int,input().split())
if k < n + m - 1:
    print('NO')
else:
    print("YES")
    for i in range(n):
        line = []
        for j in range(m):
            line.append(1+i+j)
        print(*line)