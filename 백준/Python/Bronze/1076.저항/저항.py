color1={'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}

ans=(color1[input()])
ans*=10
ans+=(color1[input()])
ans*=10**(color1[input()])

print(ans)
