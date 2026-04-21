a = int(input())

if a == 1:
    print(11)
    print('A B C D E F G H J L M')
elif a in range(2,5):
    print(9)
else:
    print(8)

if a in range(2,4):
    print('A C E F G H I L M')
elif a == 4:
    print('A B C E F G H L M')
elif a in range(5,10):
    print('A C E F G H L M')
elif a == 10:
    print('A B C F G H L M')
