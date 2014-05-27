import json
class ComplexEncoder(json.JSONEncoder):
   def default(self, obj):
      print "in defaults"
      if isinstance(obj, complex):
         return [obj.real, obj.imag]
      return json.JSONEncoder.default(self, obj)

   def encode(self, obj):
      # import pdb; pdb.set_trace()
      print "in encode"
      if obj is int:
         return obj
      return json.JSONEncoder.encode(self, obj)

print json.dumps(2 + 1j, cls=ComplexEncoder)
print json.dumps(True, cls=ComplexEncoder)
print ComplexEncoder().encode(2 + 1j)
print ComplexEncoder().encode(2)
print ComplexEncoder().encode(True)
print list(ComplexEncoder().iterencode(2 + 1j))

from collections import defaultdict

class MethodStatEncoder(json.JSONEncoder):
   def default(self, obj):
      print "in defaults"
      print type(obj)
      if isinstance(obj, complex):
         return [obj.real, obj.imag]
      if isinstance(obj, MethodStat):
         return {"totalTime" : obj.totalTime, "count" : obj.count}

      return json.JSONEncoder.default(self, obj)

   def encode(self, obj):
      # import pdb; pdb.set_trace()
      print "in encode"
      if obj is int:
         return obj
      return json.JSONEncoder.encode(self, obj)

class MethodStat(object):
   def __init__(self):
      self.totalTime = 0
      self.count = 0

   def addTime(self, timeTaken):
      self.totalTime += timeTaken
      self.count += 1

   def __repr__(self):
      return json.dumps(self.__dict__)

print '---------'
stats = defaultdict(MethodStat)

stats["key1"].addTime(10)
stats["key1"].addTime(10)
stats["key2"].addTime(10)
print '---------'
print json.dumps(stats, cls=MethodStatEncoder)
