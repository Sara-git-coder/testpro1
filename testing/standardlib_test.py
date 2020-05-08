import math
import os
import random
from datetime import date
import datetime
import time

now = date.today()
print(now)
print (time.asctime ())
print (time.time ())
print (time.localtime ())
print (time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime ()))
print (datetime.datetime.now ().strftime("%Y-%m-%d %H:%M:%S"))
nowtime = datetime.datetime.now()
yes_time = nowtime + datetime.timedelta(weeks=3)
print(yes_time.strftime("%Y-%m-%d %H:%M:%S"))
# print (os.path.exists ("test"))
# if not os.path.exists('test'):
#     os.mkdir('test')
# if not os.path.exists('test/test.txt'):
#     f = open('test/test.txt','w')
#     f.write("hello,welcome luxiuxiu")
#     f.close()


# print (os.getcwd ())
# print (os.system ('mkdir today'))
# os.removedirs('today')
# print (dir (os))
# print (math.log2 (1024))
# print (math.log (1024, 2))
# print (random.choice (['apple', 'orange', 'banana']))
# print (random.sample (range (100), 10))
# print (random.random ())
# print (random.randrange (1000))

# print (math.ceil (4.5))
# print (math.floor (4.8))
# print (math.sqrt (1024))