from datetime import datetime

print(dir(datetime))
now = datetime.now()
print(now)
day = now.day
year = now.year
month = now.month
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print("timestamp", timestamp)
print(f"{day}/{month}/{year}, {hour}:{minute}")

new_year = datetime(2020, 1, 1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)  # 1 1 2020 0 0
print(f"{day}/{month}/{year}, {hour}:{minute}")  # 1/1/2020, 0:0


now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time: ", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time one:", time_one)
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
