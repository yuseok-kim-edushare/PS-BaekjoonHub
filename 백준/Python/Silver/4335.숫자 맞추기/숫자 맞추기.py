import sys
input=sys.stdin.readline

number=99
reply='0'
logReply=[0]*11
while number!=0:
    switch=False
    while reply!='right on':
        number=int(input())
        if number==0:
            break
        reply=input().rstrip()
        if reply=='too high':
            if logReply[number]==-1:
                switch=True
            logReply[number]=1
        elif reply=='too low':
            if logReply[number]==1:
                switch=True
            logReply[number]=-1
        else:
            if logReply[number]!=0:
                switch=True
            logReply[number]=2
    else:
        reply='0'
        if switch:
            print('Stan is dishonest')
        else:
            for i in range(1,11):
                if i<number:
                    if logReply[i]==1:
                        switch=True
                else:
                    if logReply[i]==-1:
                        switch=True
            if switch:
                print('Stan is dishonest')
            else:
                print('Stan may be honest')
        logReply=[0]*11