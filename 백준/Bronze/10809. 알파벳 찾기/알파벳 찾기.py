data=input()

alpha=list(map(chr, range(ord('a'), ord('z')+1)))

ans=''

for x in alpha:

    d = ''

    if data.count(x)>0:

        d=data.index(x)

    else:

        d='-1'

    ans=ans+str(d)+' '

print(ans.rstrip())