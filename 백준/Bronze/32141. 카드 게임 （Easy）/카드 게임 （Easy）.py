n, h = map(int, input().split())
d = list(map(int,input().split()))
count = 0
answer = -1
for x in d:
    h -= x
    count += 1
    if h<=0:
        answer = count
        break
print(answer)