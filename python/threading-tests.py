import threading
import ctypes

print threading.currentThread().getName()
print threading.currentThread().ident

# __syscall = ctypes.CDLL('libc.so.6').syscall
__syscall = ctypes.CDLL('msvcrt.dll')
import pdb;pdb.set_trace()

def gettid():
   return __syscall(224)

print gettid()