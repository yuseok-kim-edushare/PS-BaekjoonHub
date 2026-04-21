import sys
nu = sys.stdin.readline()
ns = input().split()
for i in range(0,len(ns)):
    ns[i] = int(ns[i])
minn = min(ns)
maxn = max(ns)
print(str(minn)+' '+str(maxn))