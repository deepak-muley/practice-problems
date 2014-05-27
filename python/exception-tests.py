import logging
import sys

class A(object):
   pass

try:
   raise Exception("test %s %s" % ("abc", type(A)))
   1/0
except ZeroDivisionError, e:
   print '**', e.msg, '**'
   logging.exception("exception caught %s" % 'testdata')
   print 'zero Div error'
   raise 
except Exception, e:
   print '**', e.message, '**'
   logging.exception("exception caught %s" % 'testdata')
   print 'except error %s' % e

try:
   errorState = []
   try:
      1/0
   except Exception, e:
      print e.args
      print '-------'
      print e
      print '-------'
      logging.exception("******test %s", e.args)
      print '-------'
      logging.error("test %s", e.args, exc_info=True)
      print '-------'
      
      print "org" , sys.exc_info()
      etype, t = sys.exc_info()[:2]
      errorState.append((etype, t))
      print "-----", type(etype)

      try:
         raise RuntimeError("test")
      except:
         print "new", sys.exc_info()   
         pass
      print "?1=", sys.exc_info()   
      raise
except Exception, e:
   print "?2=", sys.exc_info()   
   print e   

print errorState