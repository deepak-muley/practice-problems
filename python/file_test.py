#!/usr/bin/python
#http://www.tutorialspoint.com/python/python_files_io.htm

try:
	# Open a file
	fo = open("foo.txt")
	print "Name of the file: ", fo.name
	print "Closed or not : ", fo.closed
	print "Opening mode : ", fo.mode
	print "Softspace flag : ", fo.softspace
except Exception:
  	pass


# Open a file
fo = open("foo2.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");

# Close opend file
fo.close()

try:
	import os
	# Open a file
	fo = os.open("foo3.txt", os.O_RDWR)
	fo.write( "Python is a great language.\nYeah its great!!\n");

	# Close opend file
	fo.close()
except Exception:
	pass

import os, sys

# Open a file
fd = os.open( "foo4.txt", os.O_RDWR|os.O_CREAT )

# Write one string
os.write(fd, "This is test")

# Close opened file
os.close( fd )

print "Closed the file successfully!!"
