import threading
lock = threading.RLock()
q = []

def f1():
   with lock:
      q.append(1)
      with lock:
         q.append(2)

f1()
print q
