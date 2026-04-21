N, L = map(int,input().split())
a = list(map(int,input().split()))+[0]*N

tot_alchol = [a[0]]
for i in range(1, N):
    tot_alchol.append(tot_alchol[i-1] + a[i])

now_alchol = tot_alchol[0:L]
for j in range(N-L):
    now_alchol.append(tot_alchol[j + L] - tot_alchol[j])

ans=0
for k in range(len(now_alchol)):
    if now_alchol[k] in range(129,139):
        ans+=1
print(ans)
