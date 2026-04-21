t=int(input())
for x in range(t):
    n=int(input())
    f=1
    if n==0:
        pass
    else:
        for x in range(1,n+1):
            f=f*x
            while f%10==0:
                f=f//10
    print(f%10)