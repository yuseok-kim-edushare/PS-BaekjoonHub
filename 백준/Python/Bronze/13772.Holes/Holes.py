import sys
readline = sys.stdin.readline

n = int(readline())
for i in range(n):
    text = readline()
    holes = 0
    for x in text:
        if x in ["A", "D", "O", "P", "Q", "R"]:
            holes += 1
        elif x in ["B"]:
            holes += 2
    print(holes)
