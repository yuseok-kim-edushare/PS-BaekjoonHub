n = int(input())
positions = []
for _ in range(n):
    x, y = map(int,input().split())
    positions.append((x,y))
lengths = 0
current_x = x
current_y = y
for i in range(n):
    x, y = positions[i][0], positions[i][1]
    lengths += abs(x - current_x) + abs(y - current_y)
    current_x, current_y = x, y
print(lengths)