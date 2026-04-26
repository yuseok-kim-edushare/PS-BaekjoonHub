import sys

input = sys.stdin.readline
print = sys.stdout.write
ln = '\n'

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    now_a = 0
    now_b = 0
    now_c = 0
    failed = False
    for i in range(n):
        a, b, c, p = map(int,input().split())
        now_a = max(a,now_a)
        now_b = max(b,now_b)
        now_c = max(c,now_c)
        if now_a+now_b+now_c+i+1 > p:
            failed = True
    if failed:
        print('NO')
        print(ln)
    else:
        print('YES')
        print(ln)
