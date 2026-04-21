t=int(input())
for _ in range(0,t):
    n,m=map(int,input().split())
    if n==m:
        print(1)
    else:
        ans=1
        for j in range(n+1,m+1):
            ans=ans*j
        for k in range(1,m-n+1):
            ans=ans//k
        print(ans)