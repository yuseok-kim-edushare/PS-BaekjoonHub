import sys
input=sys.stdin.readline

n=int(input())
requests=list(map(int,input().split()))
t,p=map(int,input().split())
s=0
for i in requests:
    s+=i//t
    if i%t!=0:
        s+=1
print(s)
print(n//p, n%p)