def foo(b = None, assumePowerOff=False):
   print assumePowerOff

a = foo
foo(assumePowerOff = a is not None)
foo(assumePowerOff = a is None)
foo(assumePowerOff = (a is not None))


def foo(x, y):
   print x, y

print foo.func_code
print foo.func_code.co_varnames
print foo.func_code.co_argcount
