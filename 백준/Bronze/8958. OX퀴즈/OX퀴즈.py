n=int(input())
for x in range(0,n):
    st=input()
    c=1
    score=0
    for t in range(0,len(st)):
        if st[t]=='O':
            score = score + c
            c = c+1
        elif st[t]=='X':
            c=1
        if t==len(st)-1:
            print(score)
            score=0
    