word = list(input())
answer = 0
if word == list(reversed(word)):
    answer = len(word)
else:
    x = len(word) - 1
    while answer == 0:
        now_range = len(word) - x
        for i in range(now_range + 1):
            a = list(word[i:i+x])
            b = list(reversed(word[i:i+x]))
            if a == b:
                answer = x
        if answer == 0:
            x -= 1
    
print(answer)
