p=int(input())
c=int(input())
score=50*p-10*c
if p>c:
    score=score+500
print(score)