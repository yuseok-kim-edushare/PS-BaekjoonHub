n = int(input())

score = input().split()

for i in range(0,len(score)):

    score[i]=int(score[i])

m = max(score)

for i in range(0,len(score)):

    score[i]=score[i]/m*100

print((sum(score)/len(score)))