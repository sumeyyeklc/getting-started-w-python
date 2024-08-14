from datetime import date

today = date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday()) 
print(today.isoweekday()) #starts the week from monday

past = date(2014,9,24)
print(past.weekday())
