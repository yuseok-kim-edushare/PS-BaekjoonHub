word=input()
l=len(word)
ans=[]
for i in range(1,l-1):
    for j in range(1,l-i):
        a=word[0:i]
        b=word[i:i+j]
        c=word[i+j:]
        t=a[::-1]+b[::-1]+c[::-1]
        ans.append(t)
ans.sort()
print(ans[0])