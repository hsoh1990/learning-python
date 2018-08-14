import time
import datetime

print(time.time())
print(time.gmtime())
print(time.localtime())
print(time.gmtime().tm_year)

t1 = time.time()
time.sleep(2)
t2 = time.time()
print(t2 - t1)

print(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime()))
print(time.strftime('%y.%m.%d %I:%M:%S %A', time.localtime()))

birthday = datetime.date(1990, 8, 16)
print(birthday)
print(birthday.month)

current_time = datetime.time(14, 40, 00)
print(current_time)

birthday = datetime.datetime(1990, 8, 16, 18, 30, 20)
print(birthday)
print(birthday.weekday())
print(birthday.isoformat())

print(birthday + datetime.timedelta(days=-1))
