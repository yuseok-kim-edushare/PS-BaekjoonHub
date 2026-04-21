import math
a,b = map(int,input().split())
s='1'*math.gcd(a,b)
print(s)