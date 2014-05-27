import collections

class ScsiLUN(object):
   def fn1(self):
      print "fn1"
      return 1

   def fn2(self, a, b, c):
      print "fn2 %s" % (a+b)
      return a+b

l = [A(), A()]

def onAll(l, funcs):
   for o in l:
      for order, fargs in funcs.iteritems():
	 print order
         if hasattr(o, fargs['fname']):
            getattr(o, fargs['fname'])(*fargs['args'], **fargs['kwargs'])

  
d = {'1' : {'fname': 'fn1', 'args':[], 'kwargs': {}}, 
     '2' : {'fname': 'fn2', 'args':[10], 'kwargs': {'b' : 1, 'c': 2}}
	   }
onAll(l, collections.OrderedDict(sorted(d.items(), key=lambda t: t[0])))

