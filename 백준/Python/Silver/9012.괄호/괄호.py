n=int(input())
for x in range(0,n):
    data=input()
    p=0
    test=True
    for k in range(0,len(data)):
        if data[k]=='(':
            p=p+1
        else:
            p=p-1
        if p<0:
            test=False
    if p!=0:
        test=False
    if test:
        print('YES')
    else:
        print('NO')