import sys
n = int(sys.stdin.readline().rstrip())
if n==0:
    print(0)
else:
    rates=[]
    s=0
    for i in range(0,n):
        rates.append(int(sys.stdin.readline().rstrip()))
    if n<4:
        print(int((sum(rates)/n)+0.5))
    else:
        s=int(0.5+n*0.15)
        rates.sort()
        rates=rates[s:-s]
        print(int(0.5+(sum(rates)/(n-2*s))))