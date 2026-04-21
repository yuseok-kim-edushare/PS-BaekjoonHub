import sys
n = int(input())
i = 0
a=[]
l=0
while i<n:
    i = i+1
    op = sys.stdin.readline().rstrip()
    if op =='size':
        print(l)
    elif op =='empty':
        if 0==l:
            print(1)
        else:
            print(0)
    elif op == 'front':
        if 0==l:
            print(-1)
        else:
            print(a[0])
    elif op == 'back':
        if 0==l:
            print(-1)
        else:
            print(a[l-1])
    elif op[0:4]=='push':
        if op[5:9]=='back':
            a=a+[int(op[10:])]
            l=l+1
        else:
            a=[int(op[11:])]+a
            l=l+1
    else:
        if 0==l:
            print(-1)
        elif op[4:8]=='back':
            print(a[l-1])
            l=l-1
            a=a[:-1]
        else:
            print(a[0])
            l=l-1
            a=a[1:]