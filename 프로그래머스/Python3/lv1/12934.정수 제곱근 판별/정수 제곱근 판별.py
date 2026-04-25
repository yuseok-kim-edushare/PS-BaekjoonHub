def solution(n):
    if n ** 0.5 == int(n ** 0.5):
        answer = (1 + n ** 0.5) ** 2
    else:
        answer = -1
    return answer