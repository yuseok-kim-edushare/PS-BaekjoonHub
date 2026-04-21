import sys
input=sys.stdin.readline
n=int(input())
f=int(input())
ret=n%f
tails=n%100
ans='00'
if ret==0:
    if tails==0:
        pass
    else:
        temp=tails%f
        ttemp=tails//f
        preans=tails-(ttemp*f)
        if preans<10:
            ans='0'+str(preans)
        else:
            ans=str(preans)
else:
    tails=tails-ret
    temp=tails%f
    ttemp=tails//f
    preans=tails-(ttemp*f)
    if preans<10:
        ans='0'+str(preans)
    else:
        ans=str(preans)  
print(ans)