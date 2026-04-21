import sys
input=sys.stdin.readline

n=int(input())
rights=0
tries=0
winner=set()
user={}
for x in range(n):
    info=list(input().split())
    if info[1]!='megalusion':
        if info[1] in user:
            user[info[1]]+=1
        else:
            user[info[1]]=1
        if info[1] in winner:
            pass
        elif info[2]=='4':
            rights+=1
            tries+=user[info[1]]
            winner.add(info[1])
if rights==0:
    print(0)
else:
    print(100*rights/tries)