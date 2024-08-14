from datetime import timedelta
from datetime import datetime

current_time = datetime.now()
t_delta = timedelta(days=26,hours=4,seconds=15)
print(current_time + t_delta)