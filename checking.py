import datetime
data = str(datetime.datetime.now())
data1 = data.split(" ")
time = data1[1]
date = data1[0]
print(f"time {time} date{date}")
