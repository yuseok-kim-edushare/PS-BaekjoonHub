import sys
readline = sys.stdin.readline

n = int(readline())
for i in range(n):
    d, f, p = map(float, readline().split())
    ans = d * f * p
    print("${0:0.2f}".format(ans))
