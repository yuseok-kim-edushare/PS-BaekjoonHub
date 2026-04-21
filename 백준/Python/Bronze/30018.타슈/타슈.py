n = int(input())
a = input().split()
b = input().split()
positives = 0

for i in range(n):
    a_i = int(a[i])
    b_i = int(b[i])
    diff = a_i - b_i
    if diff > 0 :
        positives = positives + diff

print(positives)