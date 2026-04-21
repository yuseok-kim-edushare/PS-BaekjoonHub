n, m = map(int, input().split())
s0 = sum(list(map(int, input().split())))
s = []
for i in range(n):
    s.append([sum(list(map(int, input().split()))), i+1])
idx = [0]
sortedS = sorted(s, reverse=True)
if sortedS[-1][0] > s0:
    pass
else:
    for x in sortedS:
        if len(idx) < m:
            if x[0]<=s0:
                idx.append(x[1])
        else:
            break
print(*idx)
