s = input()
if s[1] == '0':
    a = int(s[0:2])
    b = int(s[2:])
    print(a+b)
else:
    a = int(s[0])
    b = int(s[1:])
    print(a+b)
