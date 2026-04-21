a=int(input())
while a!=0:
    if a<=1000000:
        print(a)
    elif a<=5000000:
        print(9*a//10)
    else:
        print(8*a//10)
    a=int(input())