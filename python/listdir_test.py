#!/usr/bin/python

import os, sys

# Open a file
path = "/home/deepakm/testapps/"
dirs = os.listdir( path )
entries = os.listdir(path)
files = []
# This would print all the files and directories recursively
#import pdb;pdb.set_trace()
while len(entries) > 0:
   ent = entries.pop()
   newdir = os.path.join(path, ent) 
   if os.path.isdir(newdir):
      print "dir %s" % newdir
      innerdirs = os.listdir( newdir )
      if innerdirs:
         entries.extend(innerdirs)
   else:
      print "file: %s" % ent
      files.append(ent)
      continue

print files
    

