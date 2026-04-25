def solution(lines):
    answer = 0
    line = []
    for x in lines:
        a, b = x[0], x[1]
        line.append(list(range(a,b)))
    counts = []
    for i in range(-100, 101):
        count = 0
        for x in line:
            if i in x:
                count += 1
        counts.append(count)
    answer += counts.count(2)
    answer += counts.count(3)
    return answer