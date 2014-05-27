class A(object):
	@classmethod
	def isVM(cls):
		return True


class B(A):
	@classmethod
	def isVM(cls):
		return False

a = A()
b = B()
print a.isVM()
print b.isVM()
