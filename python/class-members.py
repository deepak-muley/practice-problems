class foo():
	def __init__(self):
		self.__i = 1
		self.b = 2
	def bar(self):
		print 'in bar'
		print self.b
		self.__bar()

	def __bar(self): 
		print 'in __bar'
		print self.__i

f = foo()
f.bar()   # this call succeeds
#f.__bar() # this call fails
print f.__i
print f.b