n = int(input())

count = [0] * 1002
count[1] = 1
count[2] = 2
count[9] = 55

for i in range(1,n+1):
    if count[i] != 0:
        pass
    else:
        count[i] = count[i-1] + count[i-2]

print(count[n]%10007)
