import sys
input = sys.stdin.readline
write = sys.stdout.write

n,m = map(int,input().split())

u,v = map(int,input().split())

texture = []
for _ in range(u):
    texture.append(input().rstrip())

method = input().rstrip()

layer = []

if n<=u and m<=v: #전체 크기가 텍스쳐와 같거나 작으면 그대로 or 잘라서
    for i in range(n):
        layer.append(texture[i][:m])

elif method == "clamp-to-edge":
    if n<=u:
        for i in range(n):
            temp_line = texture[i]
            t = m-v
            temp_line += temp_line[-1]*t
            layer.append(temp_line)
    elif m<=v:
        temp_line = ""
        for i in range(u):
            temp_line = texture[i][:m]
            layer.append(temp_line)
        for i in range(n-u):
            layer.append(temp_line)
    else:
        temp_line = ""
        for i in range(u):
            temp_line = texture[i]
            t = m-v
            temp_line += temp_line[-1]*t
            layer.append(temp_line)
        for i in range(n-u):
            layer.append(temp_line)

elif method == "repeat":
    if n<=u:
        for i in range(n):
            temp_line = texture[i]
            temp_line = (temp_line * (1+m//v))[:m]
            layer.append(temp_line)
    elif m<=v:
        for i in range(n):
            layer.append(texture[i%u][:m])
    else:
        for i in range(n):
            temp_line = texture[i%u]
            temp_line = (temp_line * (1+m//v))[:m]
            layer.append(temp_line)

else: #mirrored-repeat
    if n<=u:
        for i in range(n):
            temp_line = texture[i]
            t = list(reversed(temp_line))
            temp = ''
            for x in t:
                temp += x
            temp_line = (temp_line + temp) * int(m/v/2 +1)
            temp_line = temp_line[:m]
            layer.append(temp_line)
    elif m<=v:
        for x in list(reversed(texture)):
            texture.append(x)
        for i in range(n):
            layer.append(texture[i%(2*u)][:m])
    else:
        for j in range(u):
            temp_line = texture[j]
            temp = ''
            t = list(reversed(temp_line))
            for x in t:
                temp += x
            temp_line = (temp_line + temp) * int(m/v/2 +1)
            temp_line = temp_line[:m]
            texture[j] = temp_line
        for x in list(reversed(texture)):
            texture.append(x)
        for i in range(n):
            layer.append(texture[i%(2*u)])
            
print(*layer,sep="\n")
