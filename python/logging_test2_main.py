import logging

import logging_test2_module

# load the logging configuration

#logging.config.fileConfig('logging.ini')
print logging.logThreads

logging_test2_module.foo()
bar = logging_test2_module.Bar()
bar.bar()
