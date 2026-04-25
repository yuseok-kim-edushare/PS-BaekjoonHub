import collections
def solution(operations):
    myQ = collections.deque()
    for i in operations:
        op = i.split()
        if op[0] == "I":
            myQ.append(int(op[1]))
        else:
            if len(myQ) == 0:
                pass
            elif op[1] == '1':
                myQ.remove(max(myQ))
            else:
                myQ.remove(min(myQ))
    answer = [0, 0]
    if len(myQ) > 0:
        answer = [max(myQ), min(myQ)]
    return answer