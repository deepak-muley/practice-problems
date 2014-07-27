class A(object):
   def foo(self):
      print "inside foo"

def fn2(a):
   a.foo()

def fn3(a):
   a.FOO()

def fn1():
   a = A()
   fn2(a)
   fn3(a)


fn1()

