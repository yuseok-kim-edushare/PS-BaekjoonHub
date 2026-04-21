import sys
input = sys.stdin.readline

a, b = map(float,input().split())
aToB = b/a
bToA = a/b
t = int(input())
for _ in range(t):
    n, v = input().split()
    n = float(n)
    if v =='A':
        print(n*aToB)
    else:
        print(n*bToA)
        