import sys
input=sys.stdin.readline

N=int(input())
for x in range(N//4):
    sys.stdout.write("long ")
else:
    sys.stdout.write("int")