cowphabet = input()
heard = input()
count = 1
idx = 0
for x in heard:
    searched = cowphabet.index(x)
    if idx >= searched:
        count += 1
    idx = searched
print(count)
