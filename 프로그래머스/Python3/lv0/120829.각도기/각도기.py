def solution(angle):
    answer = 4
    if angle in range(0,90):
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle in range(91,180):
        answer = 3
    return answer