n = int(input())
a, b, c, d = map(int,input().split())
s = input()

if s[0] != "a" or s[-1] != "a":
    print("No")
else:
    memory = ""
    isYes = True
    for x in s:
        if not isYes:
            break
        if x == memory:
            isYes = False
        else:
            if x == "a":
                a -= 1
                if a<0:
                    isYes = False
                memory = x
            elif x == "b":
                b -= 1
                if b<0:
                    isYes = False
                memory = x
            elif x == "c":
                c -= 1
                if c<0:
                    isYes = False
                memory = x
            else:
                d -= 1
                if d<0:
                    isYes = False
                memory = x
                
    if isYes:
        print("Yes")
    else:
        print("No")
