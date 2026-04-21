n = int(input())
if n==1:
    print(1)
else:
    c=(n-2)//6
    if c==0:
        print(2)
    else:
        i = 3
        while c>0:
            c= c-i+1
            if c<1:
                print(i)
            else:
                i=i+1