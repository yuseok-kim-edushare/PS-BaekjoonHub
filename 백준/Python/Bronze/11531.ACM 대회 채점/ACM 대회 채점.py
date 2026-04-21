log=input()
rights=0
penalty=0
tries={}
for x in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
    tries[x]=0
while log!='-1':
    time,name,checker=log.split()
    if checker=='right':
        rights=rights+1
        time=int(time)
        penalty=penalty+time+20*tries[name]
    else:
        tries[name]=tries[name]+1
    log=input()
print(rights,penalty,sep=' ')