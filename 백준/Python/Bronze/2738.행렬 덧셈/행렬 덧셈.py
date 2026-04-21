n,m=map(int,input().split())
A=[]
B=list()
for _ in range(0,n):
    A.append(list(map(int,input().split())))
for _ in range(0,n):
    B.append(list(map(int,input().split())))
for y in range(0,n):
    for x in range(0,m):
        A[y][x]=A[y][x]+B[y][x]
for k in range(0,n):
    p=''
    for j in range(0,m):
        p=p+str(A[k][j])+' '
    print(p)