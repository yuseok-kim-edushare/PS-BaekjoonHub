a,b=map(int,input().split())
tmp1=a%b
if tmp1==0:
    print(a//b)
else:
    ans=str(a//b)+'.'
    tmp1=tmp1*10
    k=0
    while tmp1!=0 and k<2000:
        k=k+1
        ans=ans+str(tmp1//b)
        tmp1=10*(tmp1%b)
    else:
        print(ans)