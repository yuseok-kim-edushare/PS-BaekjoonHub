n = int(input())
for x in range(0,n):
    a,b = input().split()
    a='0b'+a
    b='0b'+b
    a=int(a,2)
    b=int(b,2)
    s=a+b
    s=bin(s)
    print(s[2:])