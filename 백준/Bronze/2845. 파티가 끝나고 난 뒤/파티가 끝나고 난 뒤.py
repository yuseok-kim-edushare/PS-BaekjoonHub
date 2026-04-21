l,p=map(int,input().split())
news=list(map(int,input().split()))
s=l*p
m=''
for x in range(0,5):
    m=m+str(news[x]-s)+' '
m=m.rstrip()
print(m)