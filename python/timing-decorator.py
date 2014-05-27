from functools import wraps
import time
import logging
from profilehooks import coverage, timecall, profile

log = logging.getLogger("timing")

def timeit(method):

    def timed(*args, **kw):
        st = time.time()
        result = method(*args, **kw)
        et = time.time()

        print("----------%s took %0.3f ms" % (method.__name__, ((et-st)*1000.0)))
        return result

    return timed

class Timing(object):
   '''
   Decorator to provide timing services for method calls.

   class Foo(object):
      @timing
      def bar(self):
         return "baz"
   '''
   def __init__(self, fn):
      print("inside __init__")

 
   def __call__(self, fn):
      @wraps(fn)
      def wrapper(*pargs, **kwargs):
         print("inside wrapper") 
         st = time.time()
         ret = fn(*pargs, **kwargs)
         et = time.time()
         print("%s took %0.3f ms" % (fn.__name__, ((et-st)*1000.0)))
         return ret
      return wrapper

#timing = Timing()
@coverage
@timeit
@timecall
def test10():
	print "entering test10"
	for x in range(10):
		print x
	print "exiting test10"

@timeit
@profile
def test():
	print "entering test"
	for x in range(1000):
		print x
	print "exiting test"

test()
test10()
