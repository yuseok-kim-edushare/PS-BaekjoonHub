nums=list(map(int,input().split()))
counts=[0]*7
ans=0
for i in range(0,3):
    t=nums[i]
    counts[t]=counts[t]+1
if 3 in counts:
    ans=10000+1000*counts.index(3)
elif 2 in counts:
    ans=1000+100*counts.index(2)
else:
    ans=100*max(nums)
print(ans)