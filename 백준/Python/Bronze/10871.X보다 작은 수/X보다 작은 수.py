n,x = map(int,input().split())

nums=input().split()

ans=str('')

for i in range(0,n):

    if int(nums[i])<x:

        ans= ans+nums[i]+' '

print(ans)