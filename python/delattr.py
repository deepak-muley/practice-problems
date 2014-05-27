class A(object):
   def __init__(self):
      self.__enabled = False

   def __prop1(self):
      return 'Hi'

   def __getattr__(self, name):
      print 'get' + name
      if self.__enabled and name == 'prop1':
         return object.__getattr__('__'+name)
      else:
         return None

   @property
   def enableProp1(self):
      return self.__enabled

   @enableProp1.setter
   def enableProp1(self, val):
      self.__enabled = val


a = A()
print a.prop1
a.enableProp1 = False
try:
   print a.prop1
except Exception:
   pass
a.enableProp1 = True
