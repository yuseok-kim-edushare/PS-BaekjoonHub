def solution(nums):
    case = set()
    for i in nums:
        case.add(i)
    box = len(nums)//2
    count = len(list(case))
    answer = min(box, count)
    return answer