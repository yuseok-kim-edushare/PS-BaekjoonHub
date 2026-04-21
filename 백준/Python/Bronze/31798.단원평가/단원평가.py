a, b, c = map(int,input().split())
if a == 0:
    ans = c * c - b
elif b == 0:
    ans = c * c - a
else:
    ans = int((a + b) ** (0.5))
print(ans)