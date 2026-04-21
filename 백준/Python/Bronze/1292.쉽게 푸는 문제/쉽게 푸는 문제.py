a,b=map(int,input().split())
array=[]
i=1
while len(array)<b:
    array.extend([i]*i)
    i=i+1
ans=0
for x in range(a-1,b):
    ans=array[x]+ans
print(ans)