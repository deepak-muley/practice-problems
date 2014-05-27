class A(object):

   def __init__(self):
      print "in __init__"
      self.c = 0

   def __enter__(self):
      print "entering enter %s" % self.c
      self.c += 1
      print "exiting enter %s" % self.c

   def __exit__(self, e_type, e_value, e_traceback):

      try:
         print "entering exit: %s %s %s %s" % (e_type, e_value, e_traceback, self.c)
      finally:
	self.c -= 1
      print "exiting exit %s" % self.c

a = A()
with a:
   with a:
      print "inside with"
