coc = list(map(int,input().split()))
ek = list(map(int,input().split()))
score = 1.5 + 13*(ek[0]-coc[0]) + 7*(ek[1]-coc[1]) + 5*(ek[2]-coc[2]) +3*(ek[3]-coc[3]) +3*(ek[4]-coc[4]) +2*(ek[5]-coc[5])
if score>0:
    print("ekwoo")
else:
    print("cocjr0208")
