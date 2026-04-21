n = int(input().rstrip())

for k in range(0,n):

    s0=' '*(k)

    s1='*'*(2*n-1-2*k)

    s=s0+s1

    print(s)