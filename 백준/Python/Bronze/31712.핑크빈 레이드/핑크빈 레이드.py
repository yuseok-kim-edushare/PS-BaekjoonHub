cu,du=map(int,input().split())
cd,dd=map(int,input().split())
cp,dp=map(int,input().split())
h=int(input())-du-dd-dp
c1=cu
c2=cd
c3=cp
timer=0
while h>0:
    timer=timer+1
    c1=c1-1
    c2=c2-1
    c3=c3-1
    if c1==0:
        c1=cu
        h=h-du
    if c2==0:
        c2=cd
        h=h-dd
    if c3==0:
        c3=cp
        h=h-dp
else:
    print(timer)