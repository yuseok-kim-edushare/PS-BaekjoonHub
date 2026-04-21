import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10000000)
from collections import deque

m, n = map(int, readline().split()) #상자 가로 M칸, 세로 N칸
box = []
for i in range(n):
    box.append(list(map(int, readline().split())))
    
countDays = 0 #세고 있는 날짜 수
remaining = 0 #남은 안 익은 토마토 수

queue = deque()
for i in range(n): #y축(세로 축) 범위 안에서
    for j in range(m): #x(가로) 축 범위의 토마토 상태 검사
        if box[i][j] == 1:
            queue.append((i, j)) #익은 거면 bfs 큐 목록 추가
            #세로축이 리스트 idx의 1차, 가로축이 2차 idx임에 유의
        elif box[i][j] == 0:
            remaining += 1 #안 익은 거 갯수 세기

dr = [(0, 1), (0, -1), (1, 0), (-1, 0)] #변위 목록

nextqueue = deque()
# Do BFS
def bfs():
    global remaining
    global countDays
    while queue:
        y, x = queue.popleft() #큐에서 BFS 탐색 시
        for i in range(4):
            ay, ax = dr[i][0] + y, dr[i][1] + x #변위 목록 값 불러와 적용 후 탐색 시작
            if 0 <= ax  <m and 0 <= ay < n: #이동 대상 범위가 좌표 범위 안이면
                if box[ay][ax] == 0:
                    nextqueue.append((ay,ax))
                    box[ay][ax] = 1
                    remaining -= 1
    if nextqueue:
        queue.extend(nextqueue)
        nextqueue.clear()
        countDays += 1
    if queue: bfs()

bfs()
if remaining>0:
    countDays = -1
print(countDays)
    
