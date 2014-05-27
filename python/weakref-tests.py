import weakref

o = weakref.WeakValueDictionary()
o2 = {}

class WeakList(list):
   def __del__(self):
      print "deleting %s" % self

class A(object):
   def __del__(self):
      print "deleting %s" % self

class B(object):
   def __del__(self):
      print "deleting %s" % self

a = A()
b = B()

def callback(reference):
    """Invoked when referenced object is deleted"""
    print 'callback(', reference, ')'

obj = ExpensiveObject()
r = weakref.ref(obj, callback)

def f(x, y):
   r = WeakList([x, y])
   m = [a, b]
   o[0] = r
   o2[0] = m
   print "going out of f"

f(a, b)
print len(o) # print 0
print len(o2) # print 1
