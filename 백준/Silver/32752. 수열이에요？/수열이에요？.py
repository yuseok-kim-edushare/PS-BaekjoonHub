n, l, r = map(int, input().split())
a = list(map(int, input().split()))
target = sorted(a[l-1:r])

check = True

isStarting = l==1
isEnding = r==n

if isStarting and isEnding:
    pass
elif isStarting:
    if target[-1] <= a[r] :
        pass
    else:
        check = False
elif isEnding:
    if a[l-2] <= target[0]:
        pass
    else:
        check = False
else:
    if target[-1] <= a[r]:
        if a[l-2] <= target[0]:
            pass
        else:
            check = False
    else:
        check = False
    
if check:
    print(1)
else:
    print(0)