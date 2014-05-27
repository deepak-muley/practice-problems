class ErrRetry(Exception):
   pass

class VMFSError(EnvironmentError, ErrRetry):
   pass

def firstExp():
   try:
      with open("c:\\test.txt", 'r') as f:
         data = f.read()
   except EnvironmentError, e:
      print e
      raise VMFSError(e.errno, e.strerror)


def secondExp():
   try:
      firstExp()
   except ErrRetry, e:
      print e
      raise VMFSError(e.strerror)

def thirdExp():
   try:
      secondExp()
   except ErrRetry, e:
      print e


thirdExp()
