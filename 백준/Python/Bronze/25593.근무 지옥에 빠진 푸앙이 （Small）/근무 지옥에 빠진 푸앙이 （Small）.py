import sys
input=sys.stdin.readline
print=sys.stdout.write

soldiersWorking=[]
slavesNames=[]

n=int(input())

for x in range(n):
    mornings=input().split()
    for a in mornings:
        if a=='-':
            pass
        else:
            if a not in slavesNames:
                slavesNames.append(a)
                soldiersWorking.append(4)
            else:
                t=slavesNames.index(a)
                soldiersWorking[t]=soldiersWorking[t]+4
    mids=input().split()
    for b in mids:
        if b=='-':
            pass
        else:
            if b not in slavesNames:
                slavesNames.append(b)
                soldiersWorking.append(6)
            else:
                t=slavesNames.index(b)
                soldiersWorking[t]=soldiersWorking[t]+6
    evenings=input().split()
    for c in evenings:
        if c=='-':
            pass
        else:
            if c not in slavesNames:
                slavesNames.append(c)
                soldiersWorking.append(4)
            else:
                t=slavesNames.index(c)
                soldiersWorking[t]=soldiersWorking[t]+4
    nights=input().split()
    for d in nights:
        if d=='-':
            pass
        else:
            if d not in slavesNames:
                slavesNames.append(d)
                soldiersWorking.append(10)
            else:
                t=slavesNames.index(d)
                soldiersWorking[t]=soldiersWorking[t]+10
else:
    if len(soldiersWorking)==0:
        print("Yes")
    else:
        isPair=max(soldiersWorking)-min(soldiersWorking)
        if isPair>12:
            print("No")
        else:
            print("Yes")