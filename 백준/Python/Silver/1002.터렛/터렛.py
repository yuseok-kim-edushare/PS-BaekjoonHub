import sys
input=sys.stdin.readline
n=int(input())
for _ in range(0,n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    L2=(x1-x2)**2+(y1-y2)**2
    rR=(r1+r2)**2
    rr=(r1-r2)**2
    if L2==0 and r1==r2:
        print(-1)
    elif rR>L2>rr:
        print(2)
    elif rR==L2 or rr==L2:
        print(1)
    else:
        print(0)