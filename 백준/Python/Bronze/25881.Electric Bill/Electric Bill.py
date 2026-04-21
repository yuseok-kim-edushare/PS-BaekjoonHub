import sys
input=sys.stdin.readline

rate1,rate2=map(int,input().split())
n=int(input())
for _ in range(n):
    usage=int(input())
    if usage<=1000:
        fee=rate1*usage
    else:
        fee=rate1*1000+rate2*(usage-1000)
    print(usage,fee)