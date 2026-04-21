a=input()
while a!='0':
    p=1+len(a)
    for x in a:
        if x=='1':
            p=p+2
        elif x=='0':
            p=p+4
        else:
            p=p+3
    print(p)
    a=input()