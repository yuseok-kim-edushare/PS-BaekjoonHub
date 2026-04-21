t=int(input())
for x in range(1,t+1):
    r=list(map(int,input().split()))
    r.sort()
    sw=(r[2]**2==r[0]**2+r[1]**2)
    print("Scenario #"+str(x)+":")
    if sw:
        print('yes')
    else:
        print('no')
    print()
        