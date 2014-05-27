import json
class ComplexEncoder(json.JSONEncoder):
     def default(self, obj):
         import pdb;pdb.set_trace()
         if isinstance(obj, complex):
             return [obj.real, obj.imag]
         # Let the base class default method raise the TypeError
         return json.JSONEncoder.default(self, obj)

import uuid
uid = uuid.UUID("42010998-cf1d-c7fc-7a88-15b38ee015a4")

print json.dumps(uid, cls=ComplexEncoder)
print json.dumps(2 + 1j, cls=ComplexEncoder)
print ComplexEncoder().encode(2 + 1j)
print list(ComplexEncoder().iterencode(2 + 1j))



