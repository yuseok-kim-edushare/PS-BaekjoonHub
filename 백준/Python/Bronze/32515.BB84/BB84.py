n = int(input())

base_kyung = input()
key_kyung = input()
base_ian = input()
observe_ian = input()


key = ''

for i in range(n):
    # 해킹이라면 htg! 출력 아니면 key 저장
    if base_kyung[i] == base_ian[i]:
        if key_kyung[i] == observe_ian[i]:
            key += key_kyung[i]
        else:
            print("htg!")
            base_ian = "i"*n
            break
        
if base_ian[0] != "i":
    print(key)
