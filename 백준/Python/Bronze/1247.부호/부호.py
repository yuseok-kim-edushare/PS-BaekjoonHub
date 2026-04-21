import sys
for t in range(0,3):
    n=int(input())
    s=0
    for x in range(0,n):
        s=s+int(sys.stdin.readline().rstrip())
    if s==0:
        print(0)
    elif s>0:
         print('+')
    else:
        print('-')