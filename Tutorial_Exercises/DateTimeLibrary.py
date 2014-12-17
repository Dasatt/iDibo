__author__ = 'satope'
from datetime import datetime

now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
current_hour = now.hour
current_minute = now.minute
current_second = now.second

print ("Today\'s date is: %s/%s/%s" % (current_day,current_month,current_year))
print ("The time is: %s:%s:%s" % (current_hour,current_minute,current_second))
print("We can write it together as: %s/%s/%s %s:%s:%s" %(current_day, current_month, current_year, current_hour, current_minute, current_second))
