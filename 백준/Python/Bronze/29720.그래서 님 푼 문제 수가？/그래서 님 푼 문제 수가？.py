n,k,m=map(int,input().split())
minn = str(max(0,(n-k*m)))
maxx = str(max(0,(n-k*m +(k-1))))
print(minn,maxx,sep=' ')