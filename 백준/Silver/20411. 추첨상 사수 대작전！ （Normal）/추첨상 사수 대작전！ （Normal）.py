def modexp(base, exp, moder):
    ans = 1
    while exp > 0:
        if exp % 2 == 1:
            ans *= base % moder
        base *= base % moder
        exp = exp // 2
    return ans

m, seed, x1, x2 = map(int, input().split())
a = ((x2 - x1) * modexp(x1-seed, m-2, m)) % m
c = (x1 - (a * seed)) % m
print(a, c)