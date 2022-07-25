from datetime import datetime
now=datetime.now()
year=lambda x:x.year
month=lambda x:x.month
day=lambda x:x.day
t=lambda x:x.time()

print(year(now))
print(month(now))
print(day(now))
print(t(now))
