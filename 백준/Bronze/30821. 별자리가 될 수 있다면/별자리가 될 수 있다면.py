# N 각형에서 별 갯수 -> nC_5 조합 경우의 수 
# : n! / (n-5)! / 5!
# : n * (n-1) * (n-2) * (n-3) * (n-4)
a = 1
n = int(input())
for i in range(5):
    a *= n
    n -= 1
# 5! = 5 * 4 * 3 * 2 * 1 = 120
print(a // 120)