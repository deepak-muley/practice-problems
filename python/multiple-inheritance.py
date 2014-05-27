import inspect

class BaseA:
	def A(self):
		pass

class BaseB:
	def B(self):
		pass

class C(BaseA, BaseB):
	def C(self):
		pass


print inspect.getmro(C)