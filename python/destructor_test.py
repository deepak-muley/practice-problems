class Foo:
	def __init__(self, x):
		print "Foo: Hi"
		self.x = x
	def __del__(self):
		print "Foo: bye"

print "1"
def test():
	foo = Foo(None)

test()
test()
test()
test()
#print "deleting"
#del foo
print "exiting"


