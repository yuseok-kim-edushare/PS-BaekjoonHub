import sys
input=sys.stdin.readline
write=sys.stdout.write
chars=[['' for i in range(15)] for j in range(5)]
for t in range(0,5):
    word=input().rstrip()
    for u in range(0,len(word)):
        chars[t][u]=word[u]
for x in range(0,15):
    for y in range(0,5):
        write(chars[y][x]) 