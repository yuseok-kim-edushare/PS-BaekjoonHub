n=input()
cnt = [0,0,0,0,0,
       0,0,0,0,0]
for x in n:
    i = int(x)
    cnt[i] = cnt[i] +1
o = ''
for idx in range(9,-1,-1):
    o = o+ str(idx) * cnt[idx]
print(o)