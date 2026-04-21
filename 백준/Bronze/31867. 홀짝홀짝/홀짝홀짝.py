n=int(input())
k=input()
co=0
ce=0
for x in k:
    if x in ['0','2','4','6','8']:
        ce=ce+1
    else:
        co=co+1
if co>ce:
    print(1)
elif ce>co:
    print(0)
else:
    print(-1)