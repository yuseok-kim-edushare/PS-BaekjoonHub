def checkPrime(number):
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

phone, prefix = input().split()
new = int(prefix+phone)
phone = int(phone)

if (checkPrime(phone)):
    if (checkPrime(new)):
        print("Yes")
    else:
        print("No")
else:
    print("No")