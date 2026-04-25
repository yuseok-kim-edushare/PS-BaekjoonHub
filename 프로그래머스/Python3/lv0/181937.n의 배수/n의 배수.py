def solution(num, n):
    a = num % n
    answer = 0
    if a == 0:
        answer = 1
    return answer