from functools import wraps

def devProtectionOff(fn):
   @wraps(fn)
   def wrapper(*pargs, **kwargs):
      print "calling fn %s %s" % (pargs, kwargs)
      obj = pargs[0]
      obj.wrapFn()
      fn(*pargs, **kwargs)
      print "function done"
   return wrapper

class A(object):

   def __init__(self):
      self.member = 0

   def wrapFn(self):
      print "in wrapFn"

   @devProtectionOff
   def func(self, i=0):
      print "in func %s" % i


a = A()
a.func(10)
