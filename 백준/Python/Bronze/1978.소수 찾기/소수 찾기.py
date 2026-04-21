import math

n = int(input())
nums = input().split()
count = 0
for i in range(0,n):
    if nums[i] =='1':
        count = count
    else:
        tcount = 0
        m = int(nums[i])
        tt = int(math.sqrt(m))
        for j in range(0,tt+1):
            if j==0:
                tcount=tcount
            elif m%j==0:
                tcount=tcount+1
        if tcount==1:
            count = count+1
print(count)