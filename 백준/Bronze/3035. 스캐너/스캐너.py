import sys
write = sys.stdout.write
input = sys.stdin.readline

r, c, zr, zc = map(int, input().split())
newspaper = []
for _ in range(r):
    newspaper.append(list(input()))
for i in range(r):
    for j in range(zr):
        for k in range(c):
            x = newspaper[i][k]
            for y in range(zc):
                write(x)
            if k == (c-1):
                write('\n')
