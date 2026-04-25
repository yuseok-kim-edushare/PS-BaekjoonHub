def solution(arr):
    answer = []
    idx = -1
    for i in arr:
        if idx == i:
            pass
        else:
            idx = i
            answer.append(i)
    return answer