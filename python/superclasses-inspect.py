import inspect 

class A():
    pass
class B():
    pass
class C(A, B):
    pass

def magicGetSuperClasses(cls):
    return [o[0] for o in inspect.getclasstree([cls]) if type(o[0]) == type]

def magicGetSuperClasses2(cls):
  return cls.__bases__

print magicGetSuperClasses(C)
print magicGetSuperClasses2(C)

print inspect.getmro(C)[1:]
