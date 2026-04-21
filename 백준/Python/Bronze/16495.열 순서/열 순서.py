Alphas=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
collums=input()
ans=0
b=len(collums)
for x in range(b):
    idx=(1+Alphas.index(collums[x]))
    ans+=idx*(26**(b-x-1))
print(ans)