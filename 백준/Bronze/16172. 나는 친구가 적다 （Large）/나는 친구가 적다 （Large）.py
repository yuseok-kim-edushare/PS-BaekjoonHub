a = input()
b = input()

temp = ''
for c in a:
    if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        temp += c
idx = temp.find(b)
if idx == -1:
    print(0)
else:
    print(1)
    