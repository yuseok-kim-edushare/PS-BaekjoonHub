paid = int(input())
change = 1000-paid
coin = [500,100,50,10,5,1]
coins = 0
for x in coin:
    if change>=x:
        temp = change//x
        coins = coins + temp
        change = change - x * temp
print(coins)