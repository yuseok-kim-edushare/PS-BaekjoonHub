n=int(input())
febos=[0,1]
for x in range(2,n+1):
    febos.append(febos[x-2]+febos[x-1])
ans=febos[n]
print(ans)