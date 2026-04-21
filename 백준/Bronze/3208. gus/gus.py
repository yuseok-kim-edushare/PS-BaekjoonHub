m,n=map(int,input().split())
count=0
while m*n!=0:
    direction=count%2
    if direction==0:
        m=m-1
        count=count+1
    if direction==1:
        n=n-1
        count=count+1
else:
    print(count-1)