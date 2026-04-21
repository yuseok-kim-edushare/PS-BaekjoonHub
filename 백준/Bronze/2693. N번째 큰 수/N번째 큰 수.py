import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    a=sorted(list(map(int,input().split())))
    print(a[7])