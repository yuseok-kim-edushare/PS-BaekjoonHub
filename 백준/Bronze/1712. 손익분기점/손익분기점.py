import math
a,b,c=map(int,input().split())
t = c-b
if 0>=t:
    print('-1')
else:
    print(1+a//t)