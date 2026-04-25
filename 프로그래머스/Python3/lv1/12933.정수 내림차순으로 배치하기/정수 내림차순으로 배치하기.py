def solution(n):
    count = [0,0,0,0,0,0,0,0,0,0]
    n = str(n)
    for i in n:
        count[int(i)] += 1
    answer =''
    for i in [9,8,7,6,5,4,3,2,1,0]:
        answer += str(i)*count[i]
    return int(answer)