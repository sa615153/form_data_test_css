import time
print  time.localtime(time.time())
print time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))