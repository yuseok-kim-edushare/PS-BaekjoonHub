import sys
import collections
from collections import deque
input=sys.stdin.readline
n,k=map(int,input().split())
coins=deque()
for i in range(n):
    coins.append(int(input()))
count=0
for x in range(n):
    t=coins.pop()
    count=count+(k//t)
    k=k%t
print(count)