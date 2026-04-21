x=input()
count=0
while len(x)>1:
    count=count+1
    tt=list(x)
    x=0
    for k in tt:
        x=x+int(k)
    x=str(x)
else:
    print(count)
if x in ['3','6','9']:
    print('YES')
else:
    print('NO')