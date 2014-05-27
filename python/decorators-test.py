import functools

def helloSolarSystem(original_function):
    def new_function():
        print("Calling origin function from SolarSystem")
        original_function()  # the () after "original_function" causes original_function to be called
        print("Hello, solar system!")
    return new_function
	
def helloGalaxy(original_function):
    def new_function():
        print("Calling origin function from Galaxy")
        original_function()  # the parentheses after "original_function" cause original_function to be called
        print("Hello, galaxy!")
    return new_function

@helloGalaxy
@helloSolarSystem
def hello():
    print ("Hello, world!")

# Here is where we actually *do* something!
hello()

class remoteproperty(property):
   pass

class remoteTaggedproperty(property):
   def __init__(self, *pargs, **kwargs):
      property.__init__(self, kwargs.get('fget',None),
                            kwargs.get('fset', None),
                            kwargs.get('fdel', None),
                            kwargs.get('doc', None))
      self.tags = []
      print 'remoteTaggedproperty __init__ : %s %s' %(pargs, kwargs)
      for tag in pargs:
	 if isinstance(tag, str):
	    self.tags.append(tag)
	 #else:
         #   raise AttributeError("Invalid type of tag %s" % tag)

   def __call__(self, fn):
      print "Call: %s" % fn.__name__
      return type(self)(fget=fn, fset=self.fset, fdel=self.fdel, doc=self.__doc__, *self.tags)

   def getter(self, fget):
      return type(self)(fget=fget, fset=self.fset, fdel=self.fdel, doc=self.__doc__)

   def setter(self, fset):
      return type(self)(fget=self.fget, fset=fset, fdel=self.fdel, doc=self.__doc__)

   def deleter(self, fdel):
      return type(self)(fget=self.fget, fset=self.fset, fdel=fdel, doc=self.__doc__)


class TestDecorators(object):
	@remoteproperty
	def debugprop0(self):
	   print 'Hi debugprop0'

	@remoteTaggedproperty("debug", "test", "3rdtag")
	def debugprop1(self):
	   print 'Hi debugprop1'

	@remoteTaggedproperty("debug")
	def debugprop2(self):
	   return 'Hi debugprop2'

	@debugprop2.setter
	def debugprop2(self, val): 
	   print "setting prop2 %s" % val

	@remoteTaggedproperty
	def debugprop3(self):
	   return 'Hi debugprop3'

	@remoteTaggedproperty(key='value')
	def debugprop4(self):
	   return 'Hi debugprop4'

        @debugprop4.setter
        def debugprop4(self, val):
           print "Setting: %s" % val

	def debugprop5Get(self):
	   return "Hi debugprop5"

        def debugprop5Set(self, val):
           print "debugprop5 set: %s" % val
	
	debugprop5 = remoteTaggedproperty(fget=debugprop5Get, fset=debugprop5Set)

print dir(TestDecorators)
a = TestDecorators()
a.debugprop2 = "prop2 val"
print a.debugprop2

print type(a.debugprop0)
print type(a.debugprop1)

attr1 = getattr(a.__class__, 'debugprop0', None)
attr2 = getattr(a, 'debugprop0', None)
print type(attr1)
print isinstance(attr1, remoteproperty)
print isinstance(attr2, remoteproperty)

attr1 = getattr(a.__class__, 'debugprop1', None)
attr2 = getattr(a, 'debugprop1', None)
print type(attr1)
print isinstance(attr1, remoteTaggedproperty)
a.debugprop4 = "bar"

print isinstance(attr1, remoteproperty)
print isinstance(attr2, remoteTaggedproperty)
print isinstance(attr2, remoteproperty)
print a.debugprop1
a.debugprop4 = "bar"

a.debugprop2 = "prop2 val"
print a.debugprop2

print a.debugprop5
a.debugprop5 = "test"


taggedProps = {'tag1': ['a', 'b']}
print taggedProps
taggedProps['tag1'] = ['c']
print taggedProps
l = taggedProps['tag1']
print l
l.append('e')
print taggedProps

print taggedProps.has_key('tag1')
print taggedProps.has_key('tag2')
f = taggedProps['tag1']
print f
f.append('f')
l.append('g')
print taggedProps
