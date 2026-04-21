import sys
input=sys.stdin.readline
print=sys.stdout.write

mw,mb=map(int,input().split())
tw,tb=map(int,input().split())
pw,pb=map(int,input().split())

canTw=min(tw,mb,pb)
canTb=min(tb,mw,pw)

if canTw==canTb:
    ans=canTw*2
else:
    ans=min(canTw,canTb)*2+1

print(str(ans))
