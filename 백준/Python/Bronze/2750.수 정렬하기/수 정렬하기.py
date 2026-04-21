n=int(input())
lis=[]
for x in range(0,n):
    lis.append(int(input()))
lis.sort()
for y in range(0,n):
    print(lis[y])