n = int(input())

s = -1
for _ in range(n):
    
    a, b, c = map(int, input().split())
    t = a+b+c
    if t>511:
        if t<s:
            s =t
        elif s == -1:
            s = t
        else:
            pass
print(s)
