#!/usr/bin/env python

# First import the various python modules we'll need 
import pywbem
import os
import sys
from optparse import OptionParser
 
# Some command line argument parsing gorp to make the script a little more
# user friendly.
usage = '''Usage: %prog [options]

      This program will dump the version of ESX from a host specified with 
      the -s option.'''
parser = OptionParser(usage=usage)
parser.add_option('-s', '--server', dest='server',
              help='Specify the server to connect to')
parser.add_option('-u', '--username', dest='username',
                  help='Username (default is root)')
parser.add_option('-p', '--password', dest='password',
                  help='Password (default is blank)')
(options, args) = parser.parse_args()
if options.server is None:
   print 'You must specify a server to connect to.  Use -help for usage'
   sys.exit(1)
if options.username is None:
   options.username = 'root'
if options.password is None:
   options.password = ''

# Set up the client connection object.
# Hint - With CIM XML, there is no concept of statefull sessions
#        so this call doesn't actually connect to the server.  That
#        happens later once we send a request
client = pywbem.WBEMConnection('https://'+options.server,
                               (options.username, options.password),
                               'root/cimv2')

# Now send an "Enumerate Instances" request.  This will fetch all
# instances of the specified classs (or subclasses)
l = client.EnumerateInstances('VMware_HypervisorSoftwareIdentity')
if l is None:
   print 'Error: Unable to locate any instances of VMware_HypervisorSoftwareIdentity'
else:
   # We know there's only once instance, so we can skip looping for now
   for i in l:
      print l
