h,m=map(int,input().split())
c=int(input())
m=m+c
delta=m//60
m=m%60
h=h+delta
h=h%24
print(h,m)#출력은 했어야지;;;