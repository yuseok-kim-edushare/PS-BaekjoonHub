import sys
readline = sys.stdin.readline

lotto = {}
def f(A, B, K):
    if (A, B, K) in lotto:
        return lotto[(A, B, K)]

    if A == 0 or B == 0 or K == 0: #재귀 호출 관련 Null 지정
        lotto[(A, B, K)] = 0
        return 0

    if A == B == 1:
        lotto[(A, B, K)] = 1 #<1,1>만 가능
        return 1

    else:
        temp=0
        for i in range(A):
            for j in range(B):
                if ((i & j) < K):
                    temp += 1
        lotto[(A, B, K)] = temp
        return lotto[(A, B, K)]


def new_lottery():
    A, B, K = map(int, readline().rstrip().split())
    return f(A, B, K)
    
    
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, new_lottery()))
