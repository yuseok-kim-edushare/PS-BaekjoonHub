import sys
readline = sys.stdin.readline

T = int(readline())
for _ in range(T):
    n, m = map(int, readline().split())
    prises = []
    for i in range(n):
        temp = list(map(int, readline().split()))
        k = temp[0]
        cost = temp[1:k+1]
        prises.append([temp[k+1], cost])
    prises.sort(reverse=True)
    wallet = list(map(int, readline().split()))
    net_prise = 0
    t_wallet = list(wallet)
    for x in prises:
        sw = True
        while sw:
            for a in x[1]:
                if t_wallet[a-1] == 0:
                    sw = False
                else:
                    t_wallet[a-1] -= 1
            if sw:
                net_prise += x[0]
                wallet = list(t_wallet)
            else:
                t_wallet = list(wallet)
    print(net_prise)
