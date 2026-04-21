x=int(input())
y=int(input())
xs=-1
ys=-1
if x<0:
    xs=0
if x>0:
    xs=1
if y<0:
    ys=5
if y>0:
    ys=10
s=xs+ys
if s==5:
    print(3)
elif s==6:
    print(4)
elif s==10:
    print(2)
elif s==11:
    print(1)