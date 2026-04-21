h0 = int(input())
h = h0
sw = True
while sw:
    cards = (3*h + 1)* h // 2
    if cards%4 ==0:
        sw = False
    else:
        h += 1
print(h)