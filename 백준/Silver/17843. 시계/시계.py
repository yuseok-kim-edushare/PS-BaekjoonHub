import sys
readline = sys.stdin.readline

t = int(readline())
for _ in range(t):
    h, m, s = map(int, readline().split())
    m += s / 60
    h += m / 60
    degH = 30 * h
    degM = 6 * m
    degS = 6 * s
    degrees = []
    degrees.append(degH - degM)
    degrees.append(degM - degS)
    degrees.append(degS - degH)
    for x in range(3):
        if degrees[x] < 0:
            degrees[x] *= -1
        if degrees[x] >= 180:
            degrees[x] = 360 - degrees[x]
    print(min(degrees))
