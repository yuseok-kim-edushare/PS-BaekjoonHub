import string
lowc=string.ascii_lowercase
s=input()
count=[0]*26
for c in s:
    idx=lowc.index(c)
    count[idx]=count[idx]+1
ans=''
for x in range(0,26):
    ans=ans+str(count[x])+' '
print(ans.rstrip())