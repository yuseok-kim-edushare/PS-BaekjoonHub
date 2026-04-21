import sys
input = sys.stdin.readline
write = sys.stdout.write


#초기 변수 정의
rewards = [0,0,0,0,0]

#주사위 결과 입력
n = int(input())
d = map(int,input().split())

score = 0
speed = 4
timer = 0
multi = 1

def game_init(): #게임 상태 초기화
    global score
    global speed
    global timer
    global multi
    score = 0
    speed = 4
    timer = 0
    multi = 1

def game_ender(sc): #게임 종료
    game_init()
    if sc >= 125:
        return 4
    elif sc >= 95:
        return 3
    elif sc >= 65:
        return 2
    elif sc >= 35:
        return 1
    else:
        return 0

#게임 실행
end_sig = False
for x in d:
    if x == 1 :
        end_sig = True
        idx = game_ender(score)
        rewards[idx] += 1
    elif x == 2:
        if multi > 1:
            multi = multi//2
        else:
            speed += 2
    elif x == 4:
        timer += 56
    elif x == 5:
        if speed > 1:
            speed -= 1
    elif x == 6:
        if multi < 32:
            multi *= 2
    score += multi
    timer += speed
    if timer>240 and not(end_sig):
        idx = game_ender(score)
        rewards[idx] += 1
    if end_sig:
        game_init()
        end_sig = False

        

for i in range(1,5): #1~4까지 보상 출력
    print(rewards[i])
