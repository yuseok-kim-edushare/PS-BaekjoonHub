s = int(input()) #정사각형의 넓이 값입니다.
#문제 조건: 각 점의 좌표가 정수가 되는
#주어진 넓이의 정사각형이 만들어 지도록 좌표룰 4개 출력하세요
hasIntPossition = False
sqrtS = int(s ** 0.5) +1
a = 0
b = 0
for i in range(1,sqrtS):
    tr = ((s - i*i) ** 0.5)
    if tr == tr//1:
        a = i
        b = int(tr)
        hasIntPossition = True
if hasIntPossition:
    positions = [[0,0]]
    positions.append([a,b])
    positions.append([-b,a])
    positions.append([a-b,a+b])
    for x in positions:
        print(x[0],x[1])
else:
    print("Impossible")
