# import paramiko

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect("10.241.245.180", port=22, username="root", password="P@ssw0rd123!")


# stdin, stdout, stderr = ssh.exec_command('df -kh')
# b = stdout.readlines()
# for j in b:
#     print(j)
import os

for a in range(26):
    b = 180 + a
    hostname = "10.241.245."+ str(b)
    response = os.system("ping " + hostname)

    if response == 0:
        print( hostname, 'masok pak!')
    else:
        print (hostname, 'ngadat pak!')