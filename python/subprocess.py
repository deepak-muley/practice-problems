import subprocess, commands

p=subprocess.Popen(["ls", "*"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output=p.communicate()[0]
print "o", output
result=commands.getoutput("ls *")
print "o", result