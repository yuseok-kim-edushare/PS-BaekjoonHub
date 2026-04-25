def solution(a, b, n):
    answer = 0
    while n >= a:
        count = (n//a)
        earned = b * count
        n = n % a + earned
        answer += earned
    return answer