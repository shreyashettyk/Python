import datetime
from time import strptime

#getting today date and setting a date 

some_date = datetime.date(2017,3,14)
print('the set date is ',some_date)

cur_date = datetime.datetime.today()
print('Today date is ',cur_date)

day = some_date.day
month = some_date.month
year = some_date.year
weekday = some_date.weekday()
iso_weekday = some_date.isoweekday()

print('day ',day,'month ',month,'year ',year,'weekday ',weekday,'iso weekday ',iso_weekday)

#working with timedelta

delta = datetime.timedelta(days=125)
get_future_date = datetime.datetime.today()+delta
print('the future datetime is ',get_future_date)
get_past_date = datetime.datetime.today()-delta
print('the past date is ',get_past_date)

bday = datetime.date(2085,3,14)
number_days_left = (bday-datetime.datetime.today().date()).days
print('number of days left to my bday in ',bday.year,'is ',number_days_left)


#working with today,now and utctime
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utc_now = datetime.datetime.utcnow()

print('from today ',dt_today)
print('from now ',dt_now)
print('from utc now ',dt_utc_now)

#working with strftime and strptime

#strftime - convert datetime to string format
dt = datetime.date(2020,3,14)
dt_str = dt.strftime('%B %d, %Y')
print('date in string format is ',dt_str)
print('type from strftime is ',type(dt_str))

#strptime - convert string format date time to date time format

datetime_from_str = datetime.datetime.strptime(dt_str,'%B %d, %Y')
print('string date into proper datetime ',datetime_from_str)




