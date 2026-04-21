import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dots=[]
for i in range(n):
    t=list(input().rstrip())
    dots.append(t)
cx=0
cy=0
for y in range(n):
    if 'X' in dots[y]:
        pass
    else:
        cy=cy+1
for x in range(m):
    tx=1
    for k in range(n):
        if 'X'==dots[k][x]:
            tx=0
        else:
            pass
    if tx==1:
        cx=cx+1
print(max(cx,cy))