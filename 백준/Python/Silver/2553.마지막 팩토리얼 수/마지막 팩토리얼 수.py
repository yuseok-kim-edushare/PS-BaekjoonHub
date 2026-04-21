n=int(input())
f=1
if n==0:
    pass
else:
    for x in range(1,n+1):
        f=f*x
f=str(f)[::-1]
for i in range(len(f)):
    if f[i]=='0':
        pass
    else:
        print(f[i])
        break