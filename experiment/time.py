import time

print time.localtime(time.time())
print time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

localtime = time.localtime(time.time())
print localtime
print type(localtime)


print "---------------------------------"
time_stamp_format = '%Y%m%d%H%M%S'
current_time = time.strftime(time_stamp_format)
print current_time
print type(current_time)

print "tt"
tt = time.time()
print tt
print type(tt)
print "stt"
stt = str(time.time())
print stt
print type(stt)
print "fstt"
fstt = float(stt)
print fstt
print type(fstt)
print "ifstt"
ifstt = int(fstt)
print ifstt
print type(ifstt)

print 'current_time'
print current_time

current_time = '20161228173432'
back = time.strptime(current_time,time_stamp_format)
print 'back'
print back
test = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
print 'test'
print test
print "int(time.mktime(back))"
print int(time.mktime(back))
print time.time()
# time.sleep(10)
# test = time.localtime(time.time()) - back
# print test
# print back
# print type(back)


print "\ndatetime"
from datetime import *
print timedelta(-1,1000)

# d1 = datetime(stt)
# print d1


print int(float(90000))/86400


def duration_form(seconds):
    int_second = int(seconds)
    hours = int_second/3600
    mins = (int_second - hours*3600)/60
    seconds = int_second % 60

    return str(hours) + "h " + str(mins) + "m " + str(seconds) + "s"


print duration_form(3600+72)



print int(1.2)





