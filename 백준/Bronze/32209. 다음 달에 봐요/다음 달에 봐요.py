q = int(input())
problemSetSize = 0
groupDead = False
for i in range(q):
    x, y = map(int, input().split())
    if x == 1:
        problemSetSize += y
    else:
        problemSetSize -= y
        if problemSetSize < 0:
            groupDead = True
if groupDead:
    print("Adios")
else:
    print("See you next month")