import sys
input=sys.stdin.readline

x,n=map(int,input().split())
dailyVisitors=list(map(int,input().split()))

accumulations=[dailyVisitors[0]]
for i in range(1,x):
    accumulations.append(accumulations[i-1]+dailyVisitors[i])
summations=[accumulations[n-1]]
for j in range(x-n):
    summations.append(accumulations[j+n]-accumulations[j])
m=max(summations)
if m==0:
    print("SAD")
else:
    print(str(m))
    print(str(summations.count(m)))