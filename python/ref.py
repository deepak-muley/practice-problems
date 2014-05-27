import sys

class A:
  def __init__(self, flag):
    self.flag = flag

  def func(self):
    print id(self)
    print sys.getrefcount(self)
    print self.flag

a = A(1)
print "a {0} {1}".format(id(a), sys.getrefcount(a))
b = A(2)
print "b {0} {1}".format(id(b), sys.getrefcount(b))

callback_a = a.func
callback_b = b.func
print "a {0} {1}".format(id(a), sys.getrefcount(a))
print "b {0} {1}".format(id(b), sys.getrefcount(b))
del a

print "typeof(callback_a) = {0}".format(type(callback_a))
print "typeof(callback_b) = {0}".format(type(callback_b))

print "typeof(callback_a.__func__) = {0}".format(type(callback_a.__func__))
print "typeof(callback_b.__func__) = {0}".format(type(callback_b.__func__))

print "'callback_a.__func__ is callback_b.__func__'  is {0}".format(callback_a.__func__ is callback_b.__func__)

callback_a()
callback_b()