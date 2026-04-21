import sys
n = int(input())
i = 0
a=[]
l=0
while i<n:
    i = i+1
    op = sys.stdin.readline().rstrip()
    if op =='3':
        print(l)
    elif op =='4':
        if 0==l:
            print(1)
        else:
            print(0)
    elif op == '2':
        if 0==l:
            print(-1)
        else:
            print(a[l-1])
            a.pop()
            l = l-1
    elif op == '5':
        if 0==l:
            print(-1)
        else:
            print(a[l-1])
    else:
        temp=op.split()
        t = int(temp[1])
        a.append(t)
        l=l+1