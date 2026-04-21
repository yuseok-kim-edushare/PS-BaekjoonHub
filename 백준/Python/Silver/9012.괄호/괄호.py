import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
for x in range(0,n):
    data=input().rstrip()
    p=deque()
    test=True
    for k in data:
        if k=='(':
            p.append(k)
        else:
            try:
                p.pop()
            except:
                test=False
    if len(p)>0:
        test=False
    if test:
        print('YES')
    else:
        print('NO')