scores=list(map(int,input().split()))
sMax=[100,100,200,200,300,300,400,400,500]
switch=False
for i in range(9):
    if scores[i]>sMax[i]:
        switch=True
        break
if switch:
    print('hacker')
elif sum(scores)<100:
    print('none')
else:
    print('draw')