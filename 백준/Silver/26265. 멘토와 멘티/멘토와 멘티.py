import sys
from operator import itemgetter
readline = sys.stdin.readline

mentoring=[]
n = int(readline())

for _ in range(n):
    mentoring.append(readline().split())

mentoring.sort(key=itemgetter(1), reverse=True)
mentoring.sort(key=itemgetter(0))

for a in mentoring:
    print(*a)
