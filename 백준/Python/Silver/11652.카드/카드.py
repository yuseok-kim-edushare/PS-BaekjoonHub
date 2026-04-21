import sys
input=sys.stdin.readline

n=int(input())
counting={}

for x in range(n):
    a=int(input())
    if a in counting:
        counting[a]+=1
    else:
        counting[a]=1
counting = sorted(counting.items(), key=lambda x: (-x[1], x[0]))
print(counting[0][0])
