import datetime
a=datetime.datetime.now()
a-=datetime.timedelta(9/24)
print(a.year)
print(a.month)
print(a.day)