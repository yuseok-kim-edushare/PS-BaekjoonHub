import re
n = int(input())
patterns=input().rstrip().split('*')
le=len(patterns)
p =patterns[0]+'[a-z]*'+patterns[1]
pp = re.compile(p)
for x in range(0,n):
    name=input()
    if None==re.fullmatch(pp,name):
        print("NE")
    else:
        print("DA")