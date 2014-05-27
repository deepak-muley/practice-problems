import uuid
import json

class JSONUUIDEncoder(json.JSONEncoder):

   translators = {}

   def encode(self, obj):
      try:
         obj = self.default(obj)
      except TypeError:
         pass
      return super(JSONUUIDEncoder, self).encode(obj)

   def default(self, obj):
      print obj, type(obj)
      t = type(obj)
      x = self.translators.get(t)
      if x is None:
         for k in self.translators.keys():
            if isinstance(obj, k):
               x = self.translators.get(k)
               obj = x(self, obj)
               break
      else:
         obj = x(self, obj)

      if isinstance(obj, uuid.UUID):
         return str(obj)

      return obj


def jsonEncodeDict(enc, obj):
   d = {}
   for (k, v) in obj.iteritems():
      k = enc.default(k)
      v = enc.default(v)
      d[k] = v
   return d

JSONUUIDEncoder.translators[dict] = jsonEncodeDict
JSONUUIDEncoder.translators[uuid.UUID] = lambda enc, obj: str(obj)

class JSONUUIDDecoder(json.JSONDecoder):

   def decode(self, obj):
      print "Decoding: ", obj, type(obj)
      obj = super(JSONUUIDDecoder, self).decode(obj)
      print "Decoded: ", obj, type(obj)

      keysToRemove = []
      for (k, v) in obj.items():
        keysToRemove.append(k)
        k = uuid.UUID(k)
        obj[k] = v
        
      for key in keysToRemove:
	 del obj[key]

      return obj

class JSONUUIDDecoder2(json.JSONDecoder):
   def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

   def dict_to_object(self, d):

      print "dict to object: ", d, type(d)
      obj = {}

      for (k, v) in d.iteritems():
        k = uuid.UUID(k)
        obj[k] = v
        
      return obj

uid = uuid.UUID("42010998-cf1d-c7fc-7a88-15b38ee015a4")

jsonMap= {
 uid : ["10.20.11.149", "1398978324.78"]
}

#out = json.dumps(jsonMap, cls=JSONUUIDEncoder)
#print out

out = JSONUUIDEncoder().encode(jsonMap)
print out

#d = json.loads(out)
#print d

d = JSONUUIDDecoder().decode(out)
print d

d = JSONUUIDDecoder2().decode(out)
print d
