import math
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    d=y-x
    num=int(d**0.5)
    if num==d**0.5:
        ans=num*2-1
    elif d<=num**2+num:
        ans=num*2
    else:
        ans=num*2+1
    print(ans)