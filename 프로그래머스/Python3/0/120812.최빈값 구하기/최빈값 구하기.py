def solution(array):
    answer = -2
    maxi = -1
    maxi_set = []
    for x in array:
        a = array.count(x) 
        if a >= maxi:
            if a>maxi:
                maxi_set.clear()
            if len(maxi_set)<1:
                maxi = a
                answer = x
                maxi_set.append(x)
            elif maxi_set.count(x) == 0:
                maxi_set.append(x)
    if len(maxi_set)>1:
        answer = -1
    return answer