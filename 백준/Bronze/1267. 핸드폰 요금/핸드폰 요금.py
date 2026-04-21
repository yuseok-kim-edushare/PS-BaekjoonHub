n=int(input())
calls=list(map(int,input().split()))
y=0
m=0
for x in range(0,n):
    y=y+10+(calls[x]//30)*10
    m=m+15+(calls[x]//60)*15
if y>m:
    p='M '+str(m)
elif y<m:
    p='Y '+str(y)
else:
    p='Y M '+str(y)
print(p)