n,a,b=map(int,input().split())
if a==b:
    print("Anything")
elif b<a:
    print("Subway")
elif a<b:
    print("Bus")