import sys
n=int(input())
summation=0
buf=''
try:
    x=True
    while x:
        a=sys.stdin.read(1)
        if a.isdigit():
            buf=buf+a
        else:
            summation=summation+int(buf)
            buf=''
except:
    ans=summation-(((n-1)*n)//2)
    print(ans)