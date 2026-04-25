#이 문제는 deque 쓰면 try, except 구문의 성능 이슈...
def solution(s):
    p=0
    answer = True
    for k in s:
        if k =='(':
            p=p+1
        else:
            p=p-1
        if p<0:
            answer = False
    if p!=0:
        answer = False
    return answer