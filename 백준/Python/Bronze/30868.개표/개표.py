t=int(input())
for x in range(0,t):
    n=int(input())
    a=n//5
    b=n%5
    c='++++ '*a+'|'*b
    print(c)