from decimal import Decimal, ROUND_HALF_UP

def solve():

    line = input().rstrip().split()
    
    # 모든 화폐 계산은 Decimal로 통일
    r = Decimal(line[0])
    b = Decimal(line[1])
    m = Decimal(line[2])
        
    initial_balance = b
    count = 0
        
    while b > 0:
        # 이자 계산: b * (r/100) 후 소수점 셋째 자리에서 반올림
        interest = (b * r / Decimal('100')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            
        b = b + interest - m
        count += 1
            
        # 실패 조건 1: 잔액이 줄지 않고 늘어남
        if b >= initial_balance:
            print('impossible')
            return
            
        # 실패 조건 2: 100년(1200개월) 초과
        if count > 1200:
            print('impossible')
            return
                
    print(count)


# 메인 실행부
t_str = input().rstrip()
if t_str:
    t = int(t_str)
    for _ in range(t):
        solve()
