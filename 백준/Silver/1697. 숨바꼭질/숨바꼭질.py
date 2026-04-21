from collections import deque
n, k = map(int, input().split())
posi = [-1] * 200010
posi[n] = 0
queue = deque()
queue.append(n)
while queue:
    if posi[k] == -1:
        x = queue.popleft()
        tar = [x-1, x+1, x*2]
        for i in tar:
            if i < 100002 and i > -1:
                if posi[i] == -1:
                    posi[i] = posi[x] + 1
                    queue.append(i)
    else:
        queue = deque()
print(posi[k])