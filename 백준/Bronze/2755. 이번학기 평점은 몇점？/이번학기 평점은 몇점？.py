import sys
input=sys.stdin.readline
n=int(input())
scores=0.0
credits=0.0
grades={'A+':4.3,'A0':4.0,'A-':3.7,'B+':3.3,'B0':3.0,'B-':2.7,'C+':2.3,'C0':2.0,'C-':1.7,'D+':1.3,'D0':1.0,'D-':0.7,'F':0.0}
for x in range(0,n):
    p=input().split()
    credit=float(p[1])
    credits=credits+credit
    scores=scores+credit*grades[p[2]]
avg=scores/credits+0.0005
print("{0:0.2f}".format(avg))