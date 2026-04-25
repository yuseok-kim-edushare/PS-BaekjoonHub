def solution(participant, completion):
    part_count = {}
    for i in participant:
        if i in part_count:
            part_count[i] += 1
        else:
            part_count[i] = 1
    for i in completion:
        part_count[i] -= 1
    for i in part_count:
        if part_count[i] == 1:
            answer = i
            break
    return answer