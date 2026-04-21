def fact(num):
    if num in [0,1]:
        return 1
    f=1
    for t in range(2,num+1):
        f=f*t
    return f
n,k=map(int,input().split())
x=fact(n)//(fact(k)*fact(n-k))
print(x)