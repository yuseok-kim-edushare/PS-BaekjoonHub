n,m=map(int,input().split())
cards=list(map(int,input().split()))
ans=0
for x in range(0,n):
    for y in range(1,n):
        for z in range(2,n):
            if x!=y and y!=z and z!=x:
                temp=cards[x]+cards[y]+cards[z]
                if temp>ans and m>=temp:
                    ans=temp
print(ans)