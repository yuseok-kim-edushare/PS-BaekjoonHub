n=int(input())
answer=0
for x in range(1,n):
    k=n*x+x
    answer=answer + k
print(answer)