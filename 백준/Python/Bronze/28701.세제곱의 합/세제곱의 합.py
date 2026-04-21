n = int(input())

sumN = 0
squareOfSum = 0
sumCubic = 0

for i in range(1,n+1):
    sumN += i
    sumCubic += i ** 3

squareOfSum = sumN ** 2

print(sumN)
print(squareOfSum)
print(sumCubic)