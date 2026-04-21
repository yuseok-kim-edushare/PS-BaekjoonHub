import sys
input=sys.stdin.readline
print=sys.stdout.write

x=int(input())
n=int(input())
for k in range(n):
    a,b=map(int,input().split())
    x=x-a*b
else:
    if x==0:
        print("Yes")
    else:
        print("No")
