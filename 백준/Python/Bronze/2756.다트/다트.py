t=int(input())
border=[15,12,9,6,3]
for _ in range(0,t):
    points=list(map(float,input().split()))
    player1=[]
    player2=[]
    s1=0
    s2=0
    for a in range(0,3):
        r1=(points[2*a]**2 + points[2*a+1]**2)**0.5
        r2=(points[2*a+6]**2 + points[2*a+7]**2)**0.5
        player1.append(r1)
        player2.append(r2)
    for j in player1:
        ttt=0
        for b in range(5):
            if j<=border[b]:
                ttt=20*(b+1)
        s1=s1+ttt
    for k in player2:
        tt=0
        for c in range(5):
            if k<=border[c]:
                tt=20*(c+1)
        s2=s2+tt
    sN=str(s1)
    sM=str(s2)
    ans='SCORE: '+sN+' to '+sM+', '
    if s1==s2:
        ans=ans+'TIE.'
    elif s1>s2:
        ans=ans+'PLAYER 1 WINS.'
    else:
        ans=ans+'PLAYER 2 WINS.'
    print(ans)