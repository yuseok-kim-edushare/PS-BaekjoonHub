n=int(input())
cards=list(range(1,n+1))
m=''
for x in range(0,n):
    m=m+str(cards[0])+' '
    cards=cards[1:]
    if x<n-2:
        cards=cards[1:]+[cards[0]]
m=m.rstrip()
print(m)