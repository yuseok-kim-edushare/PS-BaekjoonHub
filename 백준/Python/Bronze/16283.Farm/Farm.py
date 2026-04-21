a,b,n,w=map(int,input().split())
#w=ax+b(n-x)=(a-b)x+bn (x: sheep)
#x=(w-bn)//(a-b) (a!=b)
#if a==b, solution's cases # = p(n,2)
if n==2:
    if a+b==w:
        print(1,1)
    else:
        print(-1)
elif a==b:
    print(-1) #muti sol or fail
else:
    sheep=(w-b*n)//(a-b)
    if (a-b)*sheep!=(w-b*n):
        print(-1) #sheep isn't integer
    elif sheep<1:
        print(-1)
    elif sheep>=n:
        print(-1)
    else:
        print(sheep,(n-sheep))