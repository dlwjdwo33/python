import datetime
import time

startnowtime = datetime.datetime.now()
nowtime = datetime.datetime.now()
finishtime = startnowtime + datetime.timedelta(seconds=10)




nowtime = datetime.datetime.now()
aa = finishtime.strftime('%H:%M:%S')
bb =    nowtime('%H:%M:%S')

print aa
print bb