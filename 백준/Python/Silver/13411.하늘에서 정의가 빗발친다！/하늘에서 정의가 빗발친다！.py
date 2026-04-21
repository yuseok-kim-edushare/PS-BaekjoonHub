import sys
input=sys.stdin.readline
n=int(input())
kills=[[0,0]]*n
for i in range(0,n):
    x,y,v=map(int,input().split())
    r2=(x**2+y**2)
    kills[i]=[r2/v/v,i+1]
kills.sort()
for y in range(0,n):
    print(kills[y][1])