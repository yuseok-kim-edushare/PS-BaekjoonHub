n,k=map(int,input().split())
lis=list(map(int,input().split()))
if k==1:
    print(max(lis))
elif k==n:
    print(sum(lis))
else:
    prefix_sum=[]
    prefix_sum.append(lis[0])
    for i in range(1,n):
        prefix_sum.append(lis[i]+prefix_sum[i-1])
    stats=[]
    stats.append(prefix_sum[k-1])
    for j in range(k,n):
        stats.append(prefix_sum[j]-prefix_sum[j-k])
    print(max(stats))