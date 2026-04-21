n=int(input())
a0=input()
a=list(map(int,a0.split()))
if n==1:
    print("YES")
    print(a0)
    print(0)
else:
    delta=a[1]-a[0]
    sw=0
    for i in range(1,n):
        temp=a[i]-a[i-1]
        if temp!=delta:
            sw=1
            break
    if sw==1:
        print("NO")
    else:
        b="0 "*n
        print("YES")
        print(a0)
        print(b.rstrip())