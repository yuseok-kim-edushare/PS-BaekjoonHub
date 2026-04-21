a, b, c, n = map(int, input().split())
answer = 0
for i in range(n//a+1):
    if answer==1: break
    for j in range(n//b+1):
        if answer==1: break
        for k in range(n//c+1):
            if answer==1: break
            if a * i + b * j + c * k == n:
                answer = 1
print(answer)