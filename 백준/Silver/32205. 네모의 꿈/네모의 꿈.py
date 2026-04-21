import sys
readline = sys.stdin.readline

n = int(readline())
lengths = set()
can = False

for i in range(n):
    a = list(map(int, readline().split()))
    if not can:
        for x in a:
            if x in lengths:
                can = True
                break
            lengths.add(x)
        
if can:
    print(1)
else:
    print(0)