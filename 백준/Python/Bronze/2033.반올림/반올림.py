n=input()
a=['0','1','2','3','4']
l=len(n)
if l==1:
    print(n)
else:
    n=list(n)
    for x in range(1,l):
        if n[-x] in a:
            n[-x]='0'
        else:
            if x==l-1 and n[0]=='9':
                n=str(10**l)
            else:
                n[-x]="0"
                p=n[-x-1]
                n[-x-1]=str(1+int(p))
    print(''.join(n))