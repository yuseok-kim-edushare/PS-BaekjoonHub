n = int(input().rstrip())
for k in range(0,n):
    s0=' '*(k)
    s1='*'*(2*n-1-2*k)
    s=s0+s1
    print(s)
for x in range(1,n):
    y=n-x-1
    s0=' '*y
    s1='*'*(2*x+1)
    s=s0+s1
    print(s)