x, y, w, s = map(int, input().split())
answer =0
if s>=2*w: #대각선 이동이 직선 이동보다 2배 이상 시간 걸림 그냥 직선으로 가는게 빨라요
    answer = (x+y) * w
else:
    mini = min(x, y)
    maxi = max(x, y)
    test =[]
    test.append(w * (x + y)) #직선 이동만 씀
    test.append(mini * s + w*(maxi-mini))
    test.append(maxi * s + w*(maxi-mini))
    if x % 2 == y % 2:
        test.append(maxi * s) #만약 좌표 2개 다 홀수거나 짝수면 대각선 이동만으로 도달 가능
    else: #만약 어느 하나만 짝수라면 최고값 까지 대각선 이동하고 한칸 직선 이동 사용
        test.append(maxi * s + w)
        test.append((maxi-1) * s + w)
    answer = min(test)
print(answer)


