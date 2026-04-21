arr=[0]*10
for _ in range(0,5):
    a=int(input())
    arr[a]=arr[a]+1
for x in range(0,10):
    if arr[x] in [1,3,5]:
        print(x)