users = []
current = 0
for _ in range(10):
    off, on = map(int, input().split())
    current += (on - off)
    users.append(current)
print(max(users))