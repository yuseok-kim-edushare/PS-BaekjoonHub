x,y,w,h=map(int,input().split())
ans=min(x,abs(w-x),y,abs(y-h))
print(ans)