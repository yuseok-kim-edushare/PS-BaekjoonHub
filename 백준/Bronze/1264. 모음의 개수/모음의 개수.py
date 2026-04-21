mo=('a','e','i','o','u')
ins=input().lower()
while ins!='#':
    count=0
    for x in range(0,len(ins)):
        if ins[x] in mo:
            count=count+1
    print(count)
    ins=input().lower()