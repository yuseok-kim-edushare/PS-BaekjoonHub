n=int(input())
nums=sorted(list(map(int,input().split())))
x=int(input())
counter=0
if nums[0]>x:
    print(0)
else:
    ridx=n-1
    lidx=0
    while ridx>lidx:
        if nums[ridx]+nums[lidx]>x:
            ridx=ridx-1
        elif nums[ridx]+nums[lidx]<x:
            lidx=lidx+1
        else:
            counter=counter+1
            ridx=ridx-1
    print(counter)