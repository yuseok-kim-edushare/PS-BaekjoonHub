def facto(i):
    if i<2:
        a= 1
    else:
        a = i * facto(i-1)
    return a

print("""n e
- -----------
0 1
1 2
2 2.5
3 2.666666667
4 2.708333333""")
e = 2.70833333333
for i in range(5,10):
    e += (1 / facto(i))
    print(i, "{0:0.9f}".format(e))
