indata=input()
while indata!='0 0 0':
    p = list(map(int,indata.split()))
    p.sort()
    if p[2]*p[2]==(p[0]*p[0]+p[1]*p[1]):
        print('right')
    else:
        print('wrong')
    indata=input()