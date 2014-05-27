import subprocess, commands

p=subprocess.Popen(["ls", "*00080"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output=p.communicate()[0]
print "o", output
result=commands.getoutput("ls *00080")
print "o", result