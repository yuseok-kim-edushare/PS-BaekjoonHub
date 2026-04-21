import sys
readline = sys.stdin.readline

n = int(readline())
m = int(readline())
friendship = []
invitation = set()
friend = set()
for _ in range(m):
    friendship.append(list(map(int, readline().split())))
friendship.sort()
for x in friendship:
    if x[0] == 1:
        invitation.add(x[1])
        friend.add(x[1])
    else:
        if x[0] in friend:
            invitation.add(x[1])
        elif x[1] in friend:
            invitation.add(x[0])
invitation = list(invitation)
print(len(invitation))
    