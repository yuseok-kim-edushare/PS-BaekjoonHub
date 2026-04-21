import sys
input = sys.stdin.readline
write = sys.stdout.write

t = int(input().rstrip())

for _ in range(t):
    a, b = input().split()
    num_a = int(a)
    num_b = int(b)
    origin = num_a * num_b
    fake = ''
    la = len(a)
    lb = len(b)
    if la>lb:
        for i in range(la-lb):
            fake += a[i]
        for i in range(lb):
            fake += str(int(a[i+la-lb])*int(b[i]))
    elif la<lb:
        for i in range(lb-la):
            fake += b[i]
        for i in range(la):
            fake += str(int(a[i])*int(b[i+lb-la]))
    else:
        for i in range(la):
            fake += str(int(a[i])*int(b[i]))
    if origin == int(fake):
        print(1)
    else:
        print(0)
            
