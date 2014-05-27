class A(object):
   objList = []
   def __init__(self, a):
      self.objList.append(self)
      self.a = a

   @classmethod
   def GetMatchedObjs(cls, matcher):
      matched = []
      for obj in cls.objList:
          if matcher(obj):
             matched.append(obj)
      return matched


x = A(10)

matcherX = lambda obj: obj.a == 10
matcherY = lambda obj: obj.a == 12

print A.GetMatchedObjs(matcherX)
print A.GetMatchedObjs(matcherY)

