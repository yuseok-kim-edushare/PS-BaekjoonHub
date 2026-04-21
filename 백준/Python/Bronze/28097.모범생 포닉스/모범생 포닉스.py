n = int(input())
t = list(map(int,input().split()))
times = sum(t)+8*(n-1)
days = times // 24
hours = times % 24
print(days,hours)