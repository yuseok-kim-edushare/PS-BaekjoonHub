import sys
input=sys.stdin.readline

a=int(input())
for i in range(a):
    text=input().rstrip()
    if text[len(text)-1]!='.':
        text=text+'.'
    print(text)
