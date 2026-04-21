import sys
n = int(sys.stdin.readline().rstrip())
ns=[0]*10001
for x in range(0,n):
    k=int(sys.stdin.readline().rstrip())
    ns[k]=ns[k]+1
for t in range(1,10001):
    while ns[t]!=0:
        sys.stdout.write(str(t) + '\n')  
        ns[t]=ns[t]-1