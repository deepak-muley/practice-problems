from abc import ABCMeta

class MetaSubClassTracker(type):
   '''
   A meta-class that results in the class to which this is assigned having
   a 'subclasses' sequence that includes the set of all sub-classes of the
   class (not just direct sub-classes).

   Note that __subclasses__ won't list anything but the direct descendents of
   a particular class.

   '''

   base = type
   def __new__(mcs, name, bases, attrs):
      cls = mcs.base.__new__(mcs, name, bases, attrs)
      for base in reversed(bases):
         m = getattr(base, '__metaclass__', None)
         if m and isinstance(m, mcs.__class__):
            if not hasattr(base, 'subclasses'):
               base.subclasses = []
            base.subclasses.append(cls)
            break
      return cls


class MetaABCSubClassTracker(MetaSubClassTracker, ABCMeta):
   base = ABCMeta


class Animal(object):
    __metaclass__ = MetaSubClassTracker

    pass

class Dog(Animal):
    def talk(self):
        return "whoof whoof"

class Cat(Animal):
    def talk(self):
        return "miao"

class Pig(Animal):
    def talk(self):
        return "oink oink"

def all_animals():
    return Animal.__subclasses__()

if __name__ == "__main__":
    for animal in all_animals():
        print "%s says: %s" % (animal.__name__, animal().talk())

    print Animal.__subclasses__()
    print Animal.subclasses