n = int(input())
ans = n//5
n = n%5
if n == 0:
    print(ans)
elif n == 3:
    ans += 1
    print(ans)
elif n == 1:
    if ans<1: # 1은 처리 불가
        print(-1)
    else:
        ans += 1 #5kg 1개 풀고 3kg 2개 추가
        print(ans)
elif n == 2:
    if ans<2: #10kg 이하며 5로 나눈 나머지가 2라면 2, 7로 처리 불가
        print(-1)
    else:
        ans += 2 #5kg 2개 풀고 3kg 4개 추가
        print(ans)
elif n == 4:
    if ans<1: #4 처리 불가
        print(-1)
    else:
        ans += 2 #5kg 1개 풀고, 3kg 3개 추가
        print(ans)