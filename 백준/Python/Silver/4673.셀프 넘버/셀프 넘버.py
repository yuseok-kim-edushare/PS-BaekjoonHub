not_self=[]
nums=list(range(1,10001))
for i in nums:
    t=str(i)
    tt=i
    for x in t:
        tt=tt+int(x)
    not_self.append(tt)
for a in not_self:
    if a in nums:
        nums.remove(a)
for k in nums:
    print(k)