import threading
import time

def install_thread_excepthook():
    """
    Workaround for sys.excepthook thread bug
    (https://sourceforge.net/tracker/?func=detail&atid=105470&aid=1230540&group_id=5470).
    Call once from __main__ before creating any threads.
    If using psyco, call psyco.cannotcompile(threading.Thread.run)
    since this replaces a new-style class method.
    """
    import sys, threading
    run_old = threading.Thread.run
    def run(*args, **kwargs):
        try:
            run_old(*args, **kwargs)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            sys.excepthook(*sys.exc_info())
    threading.Thread.run = run

class ThreadWorker(threading.Thread):

    def run(self):
        print "Statement from a thread!"
        raise Dead


class Main:

    def __init__(self):
        print "initializing the thread"
	install_thread_excepthook()
        t = ThreadWorker()
        t.start()
        time.sleep(2)
        print "Did it work?"


class Dead(Exception): pass



Main()