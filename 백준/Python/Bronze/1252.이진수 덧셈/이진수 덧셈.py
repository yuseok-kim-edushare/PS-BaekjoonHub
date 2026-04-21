x,y = input().split()
x= '0b'+x
y='0b'+y
x=int(x,2)
y=int(y,2)
s=x+y
s=bin(s)
print(s[2:])