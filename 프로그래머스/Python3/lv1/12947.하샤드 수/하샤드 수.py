def solution(x):
    divider = 0
    for i in str(x):
        divider += int(i)
    return (x%divider == 0)