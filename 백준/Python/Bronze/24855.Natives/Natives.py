n = int(input())
a = sorted(list(map(int,input().split())),reverse=True)
count = n//2
a = a[:count]
print(sum(a))
