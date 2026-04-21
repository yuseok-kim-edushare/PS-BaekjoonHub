from collections import deque
n, k = map(int, input().split())
posi = [-1] * 200010
posi[n] = 0
queue = deque()
queue.append(n)
while queue:
    if posi[k] == -1:
        x = queue.popleft()
        tar = [x-1, x+1]
        for i in tar:
            if i < 100002 and i > -1:
                if posi[i] == -1 or posi[i] > posi[x]:
                    posi[i] = posi[x] + 1
                    queue.append(i)
        a = 2*x
        if a < 100001:
            if posi[a] == -1 or posi[a] > posi[x]:
                posi[a] = posi[x]
                queue.append(a)
    else:
        queue = deque()
print(posi[k])