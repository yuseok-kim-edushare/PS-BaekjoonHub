n=int(input())
counter=0
for _ in range(n):
    word=input()
    appeared=set()
    pre_char=''
    switch_0=True
    for i in word:
        if pre_char==i:
            pass
        else:
            if pre_char in appeared:
                switch_0=False
            appeared.add(pre_char)
        pre_char=i
    if pre_char in appeared: #마지막 글자 점검을 한번 더 해줘야 했어요;;
        switch_0=False
    if switch_0:
        counter=counter+1
print(counter)