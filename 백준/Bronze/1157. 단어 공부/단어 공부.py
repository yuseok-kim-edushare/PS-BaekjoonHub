import sys
word = sys.stdin.readline().upper()
alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

c = [0] * len(alp)

for i in range(0,len(alp)):

    c[i]=word.count(alp[i])

maxc = max(c)

if c.count(maxc)>1:

    print('?')

else:

    maxi = c.index(maxc)

    print(alp[maxi])