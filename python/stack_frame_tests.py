import sys
import traceback

#---------------
def one():
    two()

def two():
    three()

def three():
    for num in range(3):
        frame = sys._getframe(num)
        show_frame(num, frame)

def show_frame(num, frame):
    print frame
    print "  frame     = sys._getframe(%s)" % num
    print "  function  = %s()" % frame.f_code.co_name
    print "  file/line = %s:%s" % (frame.f_code.co_filename, frame.f_lineno)
    print "  locals    = %s" % frame.f_locals

one()

#---------------
def whoami():
    print '# this function is:', sys._getframe().f_code.co_name
    print '# this line number is:', sys._getframe().f_lineno
    print '# this file\'s name is:', sys._getframe().f_code.co_filename
 
whoami()

def get_function_name():
    return sys._getframe(1).f_code.co_name
 
def whoami():
    func_name = get_function_name()
    print '# current function\'s name:', func_name
 
whoami()

#---------------

def foo():

    for thread, frame in sys._current_frames().items():
        print('Thread 0x%x' % thread)
        traceback.print_stack(frame)

def bar():
    foo()

def baz():
    bar()

baz()
#---------------

import threading
for th in threading.enumerate():
    print(th)
    traceback.print_stack(sys._current_frames()[th.ident])
    print()

#---------------
