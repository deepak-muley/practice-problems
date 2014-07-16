def foo(b = None, assumePowerOff=False):
   print assumePowerOff

a = foo
foo(assumePowerOff = a is not None)
foo(assumePowerOff = a is None)
foo(assumePowerOff = (a is not None))
