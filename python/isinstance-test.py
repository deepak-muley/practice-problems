class A(object):
   __a = 'A'	

class B(A):
   b = 'B'


l = (B.__class__, A.__class__)
for x in l:
   print isinstance(x, l)
   print issubclass(x, A)


print hasattr(B, 'a')