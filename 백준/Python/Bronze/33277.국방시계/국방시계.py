m, n = map(int, input().split())
# 24*60 = 1440 min / day
# m/n 은 하루 중 몇 분에 해당하나? x
x = (n * 1440 // m) 
h = str(x //60)
mm = str(x % 60)
if len(h) < 2:
    h = '0'+h
if len(mm) <2:
    mm = '0' + mm

print(h+":"+mm)
