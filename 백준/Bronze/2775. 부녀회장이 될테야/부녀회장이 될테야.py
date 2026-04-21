ti=int(input())
people=[[0] * 15 for te in range(15)]
for y in range(0,15):
    people[0][y]=y
def get_pop(a,b):
    if people[a][b]!=0:
        return people[a][b]
    else:
        temp=0
        un=a-1
        for x in range(1,b+1):
            temp=temp+get_pop(un,x)
        people[a][b]=temp
        return people[a][b]
for x in range(0,ti):
    n=int(input())
    k=int(input())
    print(get_pop(n,k))