import time

#the_Time = time.ctime()
#print(the_Time)

#the_time = time.localtime()
#print(the_time)

the_time= time.localtime()
the_time2 =time.asctime(the_time)
print(the_time2)

# %Y  Year with century as decimal number
# %m  Month as a decimal number [01,12]
# %d  Day of the month as a decimal number [01,31]
# %H  Hour as a decimal number [00,23]
# %M  Minute as a decimal number [00,59]
# %S  Second as a decimal number [00,61]
# %z  Time zone offset from UTC 
# %a  Locale's abbreviated month name
# %A  Locale's full weekday name
# %B  Locale's full month name
# %C  Locale's appropriate date and time representation
# %I  Hour as a decimal number [01,12]
# %p  Locale's equivalent of either AM or PM.

timee = time.strftime("%d / %m")
print(timee)

print("started")
time.sleep(5)
print("finished")