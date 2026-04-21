n, m = map(int, input().split())
eleda = list(map(int, input().split()))
sol = list(map(int, input().split()))
cool_el = 0
cool_sol = 0
eleda.sort()
sol.sort()
eleda_count = 0
sol_count = 0
for x in eleda:
    if x>=cool_el:
        cool_el = x+100
        eleda_count +=1
for y in sol:
    if y>=cool_sol:
        cool_sol = y+360 #아 맞다 얘 쿨이 다른데;; 이거를 눈치 못 챘네요;;
        sol_count +=1
print(eleda_count, sol_count)