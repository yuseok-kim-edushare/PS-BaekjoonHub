import sys
input=sys.stdin.readline
n=int(input())
words=[]
for i in range(n):
    words.append(input().rstrip())
p=[]
l=len(words[0])
for j in range(l):
    p.append(set())
for x in range(n):
    word=words[x]
    for y in range(l):
        p[y].add(word[y])
for k in range(l):
    p[k]=list(p[k])
ans=''
for z in range(l):
    if len(p[z])==1:
        ans=ans+p[z][0]
    else:
        ans=ans+'?'
print(ans)