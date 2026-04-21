import sys
readline = sys.stdin.readline

t = int(readline())
for i in range(1,t+1):
    r, p, d = map(int, readline().split())
    ingredients = []
    std_w = 0.0
    for _ in range(r):
        name, weight, B_percent = readline().split()
        weight = float(weight)
        B_percent = float(B_percent)
        if B_percent == 100.0:
            std_w = weight
        ingredients.append([name, B_percent])
    std_w *= (d / p)
    print("Recipe # " + str(i))
    for a in range(r):
        w = ingredients[a][1] * (std_w / 100.0)
        print(ingredients[a][0], "{0:0.1f}".format(w))
    print("-"*40)