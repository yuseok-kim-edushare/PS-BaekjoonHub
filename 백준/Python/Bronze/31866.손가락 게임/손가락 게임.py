a,b=map(int,input().split())
if a==0:
    if b in [1,2,3,4]:
        print('>')
    elif b==0:
        print('=')
    else:
        print('<')
elif a==2:
    if b in [5,4,3,1]:
        print('>')
    elif b==2:
        print('=')
    else:
        print('<')
elif a==5:
    if b in [4,3,1,0]:
        print('>')
    elif b==5:
        print('=')
    else:
        print('<')
else:
    if b in [1,3,4]:
        print('=')
    else:
        print('<')