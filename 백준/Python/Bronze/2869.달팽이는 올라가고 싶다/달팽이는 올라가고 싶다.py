a,b,v=map(int,input().split())
cal=1+(v-a)//(a-b)
if (v-a)%(a-b)!=0:
    cal=cal+1 
print(cal)