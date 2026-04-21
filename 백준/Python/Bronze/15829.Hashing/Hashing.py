l = int(input())
ar = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
r=31
m=1234567891
buf=0
for i in range(0,l):
    ai = 1 + alpha.index(ar[i])
    buf = buf + ai * pow(r,i)
print(buf%m)