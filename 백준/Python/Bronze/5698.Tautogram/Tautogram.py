sentence = input()
while sentence != "*":
    sentence = sentence.lower()
    words = sentence.split()
    head = words[0][0]
    isnt = False
    for x in words:
        if x[0] != head:
            isnt = True
            break
    if isnt:
        print("N")
    else:
        print("Y")
    sentence = input()
    if sentence == "*":
        break
