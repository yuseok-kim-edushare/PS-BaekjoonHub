n=int(input())

febos=[0]*200

febos[1]=1

def febo(num):

    if num!=0 and febos[num]==0:

        febos[num]=febo(num-2)+febo(num-1)

    else:

        pass

    return febos[num]

ans=febo(n)

print(ans)