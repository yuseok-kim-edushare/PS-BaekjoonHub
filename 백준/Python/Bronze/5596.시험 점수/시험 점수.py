a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=sum(a)
n=sum(b)
if s>n:
    print(s)
else:
    print(n)