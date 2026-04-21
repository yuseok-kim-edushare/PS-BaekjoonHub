from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

start_x, start_y = 0,0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i,j
            
cnt = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs(x,y):
    
    queue = deque()
    queue.append((x,y))
    
    visited[x][y] = True
    
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while queue:
        x,y = queue.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if (0<=nx<n) and (0<=ny<m) and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    cnt[nx][ny] = cnt[x][y] + 1
                    queue.append((nx,ny))
                    

        
bfs(start_x, start_y)
cnt[start_x][start_y] = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and not visited[i][j]:
            cnt[i][j] = -1

for i in range(len(cnt)):


    print(* cnt[i])