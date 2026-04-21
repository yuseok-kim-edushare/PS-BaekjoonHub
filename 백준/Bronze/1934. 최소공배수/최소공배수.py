import math
n = int(input())
for x in range(0,n):
    a,b = map(int,input().split())
    print(math.lcm(a,b))