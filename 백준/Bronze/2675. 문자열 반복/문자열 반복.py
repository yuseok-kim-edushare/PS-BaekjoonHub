t = int(input())

i = 0

while i < t:

    r,s = input().split()

    r= int(r)

    k = 0

    b=''

    while k < (len(s)):

        b= b + s[k]*r

        k = k +1

    print(b)

    i = i+1