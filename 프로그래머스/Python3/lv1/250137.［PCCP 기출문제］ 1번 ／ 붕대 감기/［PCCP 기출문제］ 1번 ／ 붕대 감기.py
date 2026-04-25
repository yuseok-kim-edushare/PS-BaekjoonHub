def solution(bandage, health, attacks):
    HP = health
    bungdeaDuring = 0
    idxAttack = 0
    answer = 0
    last = attacks[(len(attacks)-1)][0]
    for i in range(1,last+1):
        if i == attacks[idxAttack][0]:
            HP -= attacks[idxAttack][1]
            idxAttack += 1
            bungdeaDuring = 0
            if HP <= 0:
                answer = -1
        elif HP < health:
            HP += bandage[1]
            bungdeaDuring += 1
            if bungdeaDuring == bandage[0]:
                HP += bandage[2]
                bungdeaDuring = 0
            if HP > health:
                HP = health
        if answer > -1:
            answer = HP
    return answer