from datetime import datetime, timedelta

today = datetime.now() + timedelta(hours=9)
print(today.date())
