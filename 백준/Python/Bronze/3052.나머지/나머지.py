c=[0]*42
for i in range(0,10):
    c[int(input())%42]=1
print(sum(c))