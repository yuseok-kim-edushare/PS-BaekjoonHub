a,b = input().split()
answer = ''
for i in range(min(len(a), len(b))):
    if i % 2 == 0:
        answer += a[i]
    else:
        answer += b[i]
print(answer)