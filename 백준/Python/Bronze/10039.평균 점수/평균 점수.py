sum=0
for x in range(0,5):
    t=int(input().rstrip())
    if t<40:
        t=40
    sum=sum+t//5
print(sum)