import sys
readline = sys.stdin.readline

n, m = map(int,readline().split())
friends = [0] * n
for i in range(m):
    a, b = map(int,readline().split())
    friends[a-1] += 1
    friends[b-1] += 1
print(*friends, sep='\n')
