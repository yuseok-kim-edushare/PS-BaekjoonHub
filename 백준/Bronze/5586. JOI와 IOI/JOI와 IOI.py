text=input()

cnt_joi=0
cnt_ioi=0
sw_joi=0
sw_ioi=0

for x in text:
    if x=='J':
        sw_joi=1
        sw_ioi=0 
    elif x=='O':
        if sw_joi==1:
            sw_joi=2
        else:
            sw_joi=0
        if sw_ioi==1:
            sw_ioi=2
        else:
            sw_ioi=0
    elif x=='I':
        if sw_joi==2:
            cnt_joi+=1
            sw_joi=0
        else:
            sw_joi=0
        if sw_ioi==2:
            sw_ioi=1
            cnt_ioi+=1
        else:
            sw_ioi=1
    else:
        sw_joi=0
        sw_ioi=0
print(cnt_joi)
print(cnt_ioi)
