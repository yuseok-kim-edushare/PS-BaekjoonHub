a,b,c,d = map(int,input().split())
dog1 = a+b
dog2 = c+d
p,m,n = map(int,input().split())

cp = 0
cm = 0
cn = 0

if p%dog1 in range(1,a+1):
    cp += 1
if p%dog2 in range(1,c+1):
    cp += 1

if m%dog1 in range(1,a+1):
    cm += 1
if m%dog2 in range(1,c+1):
    cm += 1

if n%dog1 in range(1,a+1):
    cn += 1
if n%dog2 in range(1,c+1):
    cn += 1

print(cp,cm,cn, sep="\n")
