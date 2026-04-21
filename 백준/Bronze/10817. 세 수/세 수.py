a,b,c=map(int,input().split())
mid=a
if b>a and c>a:
    if b>c:
        mid=c
    else:
        mid=b
if b<a and c<a:
    if b<c:
        mid=c
    else:
        mid=b
print(mid)