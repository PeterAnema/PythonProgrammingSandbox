import time
from threading import Thread
import random

def myfunc(i):
    print("sleeping x sec from thread %d" % i)
    time.sleep(random.randint(3,10))
    print("finished sleeping from thread %d" % i)

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()