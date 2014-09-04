class B(object):

   def __str__(self):
      return "class B instance __str__"

class A(object):

   def __init__(self):
      self.a = [1, 2, 3]
      self.b = B()

   def __str__(self):
      return "class A instance __str__"

   def __repr__(self):
      return "class A instance __repr__"

a = A()
print A
print a
print "%s %s %s" % (a, a.a, a.b)
