y=[0,0,0]
p=[[0,'a'],[0,'a'],[0,'a']]
for i in range(3):
    a,b,c=input().split()
    y[i]=int(b)%100
    p[i][0]=int(a)
    p[i][1]=c[0]
y.sort()
p.sort(reverse=True)
ans1=str(y[0])+str(y[1])+str(y[2])
ans2=''
for j in range(3):
    ans2=ans2+p[j][1]
print(ans1)
print(ans2)