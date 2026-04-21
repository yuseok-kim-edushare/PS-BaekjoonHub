import sys
readln = sys.stdin.readline

n = int( readln())
ppl = {}

for _ in range(n):
    x = readln().split()
    if x[1] == 'enter':
        ppl[x[0]] = True
    else:
        del ppl[x[0]]

people = list(ppl.keys())
people.sort(reverse=True)
print(*people, sep="\n")