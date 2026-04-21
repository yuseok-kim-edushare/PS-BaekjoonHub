nums=[0]*81
pos=dict()
for i in range(9):
    temps=list(map(int,input().rstrip().split()))
    for j in range(9):
        nums.append(temps[j])
        pos[temps[j]]=[i+1,j+1]
m=max(nums)
print(m)
mp=pos[m]
print(*mp)