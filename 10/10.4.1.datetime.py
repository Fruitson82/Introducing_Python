from datetime import date
from timedelta import timedelta
halloween = date(2015, 10, 31)

print(halloween)

print(halloween.day)
print(halloween.month)
print(halloween.year)

print(halloween.isoformat())

one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)