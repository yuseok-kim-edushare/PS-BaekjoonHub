ax,ay,az=map(int,input().split())
cx,cy,cz=map(int,input().split())
bz=cz-ax
by=cy//ay
bx=cx-az
print(str(bx)+' '+str(by)+' '+str(bz))