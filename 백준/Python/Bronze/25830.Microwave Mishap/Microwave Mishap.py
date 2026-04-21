hh,mm=map(int,input().split(":"))
H=hh
M=mm-hh
S=-mm
if S<0:
    M-=1
    S+=60
if M<0:
    H-=1
    M+=60
if H<10:
    H='0'+str(H)
if M<10:
    M='0'+str(M)
if S<10:
    S='0'+str(S)
print(str(H)+':'+str(M)+':'+str(S))