while True:
    o=input()
    if o=='0 0 0':
        break
    else:
        r=list(map(int,o.split()))
        r.sort()
        t=set(r)
        if r[2]>=r[0]+r[1]:
            print('Invalid')
        elif len(t)==1:
            print('Equilateral')
        elif len(t)==2:
            print('Isosceles')
        else:
            print('Scalene')
    