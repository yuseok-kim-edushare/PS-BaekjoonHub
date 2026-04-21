t=int(input())
for x in range(0,t):
    h,w,n=map(int,input().split())
    f=n%h
    r=1+(n//h)
    if f==0:
        f=h
        r=r-1
    if r<10:
        r='0'+str(r)
    print(str(f)+str(r))