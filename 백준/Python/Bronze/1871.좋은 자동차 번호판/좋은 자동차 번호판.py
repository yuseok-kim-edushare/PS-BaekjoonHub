import string
alp=list(string.ascii_uppercase)
t=int(input())
for x in range(0,t):
    one,two=input().split('-')
    two=int(two)
    a=alp.index(one[0])
    b=alp.index(one[1])
    c=alp.index(one[2])
    aa=a*26*26
    bb=b*26
    o=aa+bb+c
    if abs(o-two)>100:
        print('not nice')
    else:
        print('nice')