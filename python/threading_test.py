import logging
import threading
import time
from threading import Thread

def installThreadInit():
   print "inside install"
   init_old = threading.Thread.__init__
   def init(self, *pargs, **kwargs):
      print "inside install init"
      init_old(self, *pargs, **kwargs)
      run_old = self.run
   threading.Thread.__init__ = init

def myfunc(i):
    print "sleeping 5 sec from thread %d" % i
    time.sleep(i)
    print "finished sleeping from thread %d" % i

installThreadInit()

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    print 'joining %s' % t.getName()
    t.join()
print "end"
