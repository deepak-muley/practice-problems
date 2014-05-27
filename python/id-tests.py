class A:
	i = 10

a = A()
print id(a)

b = A()
print id(b)

b = a
print id(b)
