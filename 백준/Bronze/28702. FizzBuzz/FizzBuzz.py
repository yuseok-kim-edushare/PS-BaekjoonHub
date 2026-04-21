import sys
input=sys.stdin.readline

line1=input()
line2=input()
line3=input()

ans=''
answer=0
if line1=="Fizz" or line1=="FizzBuzz":
    ans="Fizz"
if line1[-1]=='2' or line2[-1]=='3' or line3[-1]=='4':
    ans=ans+"Buzz"
if ans=='':
    try:
        answer=1+int(line3)
    except:
        try:
            answer=2+int(line2)
        except:
            answer=3+int(line1)
    if answer%3==0:
        ans="Fizz"
    if answer%5==0:
        ans=ans+"Buzz"
    if ans=='':
        ans=str(answer)
print(ans)
