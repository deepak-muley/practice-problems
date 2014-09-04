class foo:
   def __init__(self, a, b, c):
       pass

x = foo(1, 2, 3) # __init__

class foo2:
   def __call__(self, a, b, c):
       pass

x = foo2()
x(1, 2, 3) # __call__


class A:
   def __init__(self):
      print "init"

   def __call__(self):
      print "call"

print 'instanciating'
A()
print 'calling on instance' 
A()() 
