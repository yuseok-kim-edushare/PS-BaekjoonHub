n = int(input())
cards = list(map(int,input().split()))
answer = cards[0]
index = 0
for i in range(1,n):
    if cards[index] + 1 == cards[i]:
        pass
    else:
        answer += cards[i]
    index = i
print(answer)