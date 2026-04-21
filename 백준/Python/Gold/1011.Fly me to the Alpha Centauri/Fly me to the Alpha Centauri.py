t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    d=y-x
    i=1
    temp=1
    while d>temp:
        i=i+1
        temp=temp+i//2+i%2
    print(i)