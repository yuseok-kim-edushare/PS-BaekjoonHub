def solution(ingredient):
    answer = 0
    target = [1, 2, 3, 1]
    pre_stacking = []
    for i in ingredient:
        pre_stacking.append(i)
        if len(pre_stacking) >= 4:
            if pre_stacking[-4:] == [1, 2, 3, 1]:
                pre_stacking.pop()
                pre_stacking.pop()
                pre_stacking.pop()
                pre_stacking.pop()
                answer += 1
    return answer