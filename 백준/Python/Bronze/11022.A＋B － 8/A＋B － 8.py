t = int(input())
p1='Case #'
p2=': '
p3=' + '
p4=' = '
for i in range(1,t+1):
    a,b = map(int,input().split())
    ans = str(a+b)
    print(p1+str(i)+p2+str(a)+p3+str(b)+p4+ans)
    
    