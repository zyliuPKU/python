import datetime

date='2017-12-31'
date=datetime.datetime.strptime(date,'%Y-%m-%d') #字符串生成datetime
date.day
date.month
date.year

date+=datetime.timedelta(days=1) #向后一天
date+=datetime.timedelta(days=-1) #向前一天

date.strftime('%Y-%m-%d') #datetime生成字符串

time='2017-12-31 15:00:00'
time=datetime.datetime.strptime(time,'%Y-%m-%d %H:%M:%S') #字符串生成datetime
time.hour
time.minute
time.second

time+=datetime.timedelta(hours=1)

date.strftime('%Y-%m-%d %H:%M:%S') #datetime生成字符串

ds=time.timestamp() #datetime生成时间戳
datetime.datetime.fromtimestamp(ds) #时间戳生成datetime格式

time2=datetime.datetime.strptime('2018-01-01 15:00:00','%Y-%m-%d %H:%M:%S')
dt=time2-time #时间差格式
dt.days
dt.hours
