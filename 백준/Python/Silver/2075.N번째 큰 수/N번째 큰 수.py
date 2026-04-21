import sys
readline = sys.stdin.readline

n = int(readline())

numbers = []
for _ in range(n):
    number = list(map(int,readline().split()))
    for x in number:
        numbers.append(x)
    numbers.sort(reverse = True)
    numbers = numbers[:n]

print(numbers[-1])
    