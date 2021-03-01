from datetime import datetime

now = datetime.now()
print(now, type(now))

# 构造一个datetime.datetime对象
dt = datetime(2016, 8, 1, 17, 7, 33, 34324)
print(dt)

# datetime和timestamp相互转换
dts = dt.timestamp()
print(dts, type(dts))
dt = datetime.fromtimestamp(dts)
print(dt, type(dt))

# str和datetime相互转换
t = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(t)
print(t.strftime('%a, %b %d %H:%M'))
