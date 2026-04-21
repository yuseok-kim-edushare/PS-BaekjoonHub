n = int(input().rstrip())
for x in range(0,n):
    y=n-x-1
    s0=' '*y
    s1='*'*(2*x+1)
    s=s0+s1
    print(s)