t=input().split()
a=list(t[0])
b=list(t[1])
amin=''
amax=''
bmin=''
bmax=''
for x in a:
    if x=='5':
        amax=amax+'6'
        amin=amin+x
    elif x=='6':
        amax=amax+x
        amin=amin+'5'
    else:
        amax=amax+x
        amin=amin+x
for x in b:
    if x=='5':
        bmax=bmax+'6'
        bmin=bmin+x
    elif x=='6':
        bmax=bmax+x
        bmin=bmin+'5'
    else:
        bmax=bmax+x
        bmin=bmin+x
mini=int(amin)+int(bmin)
maxi=int(amax)+int(bmax)
print(mini, maxi)