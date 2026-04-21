n=[0,0]
num=int(input())
if num<10:
    n[1]=num
elif num==0:
    pass
else:
    n[0]=num//10
    n[1]=num%10
d1=n[0]
d2=n[1]
s=d1+d2
d1=d2
d2=s%10
count=1
while d1!=n[0] or d2!=n[1]:
    s=d1+d2
    d1=d2
    d2=s%10
    count=count+1
print(count)