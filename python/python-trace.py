import sys

@sys.settrace
def trace_debug(frame, event, arg):
    if event == 'call':
        print ("calling %r on line %d, vars: %r" % 
                (frame.f_code.co_name, 
                 frame.f_lineno,
                 frame.f_locals))
        return trace_debug
    elif event == "return":
        print "returning", arg

def fun1(a, b):
    return a + b

print fun1(1, 2)
