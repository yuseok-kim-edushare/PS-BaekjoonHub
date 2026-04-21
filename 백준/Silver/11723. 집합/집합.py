import sys
m=int(sys.stdin.readline().rstrip())
s=[0]*21
for x in range(0,m):
    com=sys.stdin.readline().rstrip().split()
    if com[0]=='all':
        s=[1]*21
    if com[0]=='empty':
        s=[0]*21
    if com[0]=='add':
        s[int(com[1])]=1
    if com[0]=='remove':
        s[int(com[1])]=0
    if com[0]=='check':
        print(s[int(com[1])])
    if com[0]=='toggle':
        t=int(com[1])
        if s[t]==0:
            s[t]=1
        else:
            s[t]=0