d,h,w=map(int,input().split())
x=d/((h*h+w*w)**(0.5))
hh=h*x//1
ww=w*x//1
print(str(int(hh))+' '+str(int(ww)))