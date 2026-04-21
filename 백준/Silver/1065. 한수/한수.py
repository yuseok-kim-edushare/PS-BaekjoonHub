n = int(input())
cnt = 0

for i in range(1, n+1):
    a = str(i)
    l_a = len(a) # 이거 느리면 i 크기 기준 if elif 분기로 하드코딩 예정
    d = -15 #자리수 값 끼리 차이니 -15면 초기화로 적당함
    prev = -1 #자리수의 값이니 -1이면 초기화로 적당함
    passed = True
    for j in range(l_a):
        x = int(a[j])
        if prev == -1:
            prev = x
        else:
            y = prev - x
            prev = x
            if d != y and d != - 15:
                passed = False
            else:
                d = y   
    if passed:
        cnt = cnt + 1

print(cnt)