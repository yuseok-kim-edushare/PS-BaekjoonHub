n=int(input())//3
count=0
for x in range(1,n-1):
    for y in range(1,n-1):
        if x+y<n:
            count=count+1
print(count)
