import paramiko

host = '10.20.14.238'
userName = 'root'
pwd='d1srupt2013'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=userName, password=pwd)

stdin, stdout, stderr = ssh.exec_command("uptime")
print type(stdin)
print stdout.readlines()

stdin, stdout, stderr = ssh.exec_command("sudo dmesg")
stdin.write(pwd+'\n')
stdin.flush()
data = stdout.read().splitlines()
for line in data:
    if line.split(':')[0] == 'AirPort':
        print line


ftp = ssh.open_sftp() 
ftp.get('remotefile.py', 'localfile.py') 
ftp.close()
