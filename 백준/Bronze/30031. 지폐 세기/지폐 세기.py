t = int(input())
a = 0
for i in range(t):
    b, c = map(int,input().split())
    if b == 136:
        a += 1000
    elif b == 142:
        a += 5000
    elif b == 148:
        a+= 10000
    else:
        a += 50000
print(a)