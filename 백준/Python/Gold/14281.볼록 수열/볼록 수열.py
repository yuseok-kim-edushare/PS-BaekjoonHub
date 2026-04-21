n = int(input())
a = list(map(int, input().split()))
count = 0
isntConvex = True
while isntConvex:
    isntConvex = False
    for i in range(1,n-1):
        if a[i-1] + a[i+1] < a[i] *2:
            isntConvex = True
            diff = (a[i-1] + a[i+1]) // 2
            count += (a[i] - diff)
            a[i]=diff
print(count)