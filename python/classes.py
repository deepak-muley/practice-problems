import logging
log = logging.getLogger("test")

class A(object):
	aClassVar = 'aClassVar'
	def m1(self):
		print "A.m1"
		print self.aClassVar
#		a = 1/0

class B(A):
	def m1(self):
		super(B, self).m1()
		print "B.m1"
#		raise RuntimeError("error")

try:
	A().m1()
#except IOError, r:
#	log.exception("logging ioerror exception")

except:
	log.exception("logging exception")
B().m1()
a = A()
import pdb;pdb.set_trace()
