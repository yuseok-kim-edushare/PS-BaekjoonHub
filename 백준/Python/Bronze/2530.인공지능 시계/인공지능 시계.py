h,m,s=map(int,input().split())
d=int(input())
s=s+d
tmp=0
if s>59:
    tmp=s//60
    s=s%60
    m=m+tmp
if m>59:
    tmp=m//60
    m=m%60
    h=h+tmp
if h>23:
    h=h%24
ans=str(h)+' '+str(m)+' '+str(s)
print(ans)