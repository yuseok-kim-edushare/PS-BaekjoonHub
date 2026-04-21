a = int(input())
b = int(input())
c = int(input())

a = bin(a)[2:]
b = bin(b)[2:]
c = bin(c)[2:]

if len(a)<4:
    ped = 4 - len(a)
    a = "0"*ped + a
if len(b)<4:
    ped = 4 - len(b)
    b = "0"*ped + b
if len(c)<4:
    ped = 4 - len(c)
    c = "0"*ped + c

temp = a[-4:] + b[-4:] + c[-4:]

temp = int(temp, 2)

temp = str(temp)

if len(temp)<4:
    ned = 4-len(temp)
    temp = "0"*ned+temp

print(temp)
