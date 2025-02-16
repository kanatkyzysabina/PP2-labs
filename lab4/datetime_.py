from datetime import datetime, timedelta
#1 
current = datetime.now()
newdate = current - timedelta(days=5)
print(f"Current date: {current.strftime("%Y.%m.%d")}")
print(f"Date after subtracting 5 days: {newdate.strftime("%Y.%m.%d")}")

#2
today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(f"Yesterday's date: {yesterday.strftime('%d.%m.%Y')}")
print(f"\nToday's date: {today.strftime('%d.%m.%Y')}")
print(f"Tomorrow's date: {tomorrow.strftime('%d.%m.%Y')}")

#3
date = datetime.now()
newdate = date - timedelta(microseconds=date.microsecond)

print(f"\nDate: {date}")
print(f"Date without microseconds: {newdate}")

#4
date1 = datetime.strptime(input("Print 1 date (YYYY-MM-DD HH:MM:SS): "), "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(input("Print 2 date (YYYY-MM-DD HH:MM:SS): "), "%Y-%m-%d %H:%M:%S")

difference = date1-date2
print(f"Difference in second is: {abs(difference.total_seconds())}")
