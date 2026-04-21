box=[180]
for x in range(720):
    m=6*x
    h=6*(x//12)
    box.append(abs(m-h)%180)
box=list(set(box))
a=0
while a!=-1:
    try:
        a=int(input())
    except :
        a=-1
    if a in box:
        print("Y")
    elif a!=-1:
        print("N")