n=input()
l=len(n)
n=int(n)
const=0
x=n
end=0
if n>1000:
    end=n-9*l
while x>end:
    temp=x
    k=str(x)
    for t in range(0,len(k)):
        temp=temp+int(k[t])
    if n==temp:
        const=x
    x=x-1
print(const)