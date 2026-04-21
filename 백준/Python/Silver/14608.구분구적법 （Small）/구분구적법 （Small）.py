order=int(input())
c=list(map(int,input().split()))
c.reverse()
a,b,n=map(int,input().split())
dx=(b-a)/n
epslion=dx/2

def fx(order,x):
    y=0
    for i in range(order+1):
        y+=c[i]*(x**i)
    return y

integrate=0
for i in range(order+1):
    t=i+1
    integrate+=c[i]*((b**t-a**t)/t)

summation=0
for k in range(n):
    summation+=dx*fx(order,a+k*dx+epslion)
delta=summation-integrate

while (abs(delta/integrate)>0.0001):
    if delta<0:
        epslion=(epslion+b)/2
    else:
        epslion=(epslion+a)/2
    summation=0
    for k in range(n):
        summation+=dx*fx(order,a+k*dx+epslion)
    delta=summation-integrate

print(epslion)
