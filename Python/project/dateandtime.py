
from datetime import date
 
my_date = date(1996, 12, 11)
 
print("Date passed as argument is", my_date)
today = date.today()
 
print("Today's date is", today)
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)