n=int(input())
stand=0
count=0
idx=-1
costs=[]
for k in range(0,n):
    dc=input().split()
    c=int(dc[1])
    if idx!=-1:
        if c>stand:
            count=count+1
    else:
        costs.append(c)
    if dc[0]=='jinju':
        stand=c
        idx=k
        for x in range(0,k):
            if costs[x]>stand:
                count=count+1
print(stand)
print(count)