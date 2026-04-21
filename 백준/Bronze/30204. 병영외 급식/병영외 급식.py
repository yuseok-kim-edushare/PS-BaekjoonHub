n, x = map(int,input().split())
p = list(map(int,input().split()))
ii = 0
ss =0
while ii<n:
    ss =ss+ p[ii]%x
    ii=ii+1
if ss%x==0:
    print(1)
else:
    print(0)