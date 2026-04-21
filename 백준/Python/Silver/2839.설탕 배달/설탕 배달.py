n=int(input())
counter=[-1]*5001
counter[3]=1
counter[5]=1
idx=6
while idx<=n:
    if counter[idx] !=-1:
        pass
    else:
        if counter[idx-3] !=-1:
            counter[idx]=counter[idx-3]+1
            counter[idx]
        if counter[idx-5] != -1:
            counter[idx]=counter[idx-5]+1
    idx=idx+1
print(counter[n])