v = int(input())
votes = input()
cnt_a = votes.count("A")
if cnt_a > v - cnt_a:
    print("A")
elif cnt_a * 2 == v:
    print("Tie")
else:
    print("B")