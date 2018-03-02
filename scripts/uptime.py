import paramiko
def getuptime(x):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(x,username='albany_ccn1',password='12345')
    stdin,stdout,stderr=ssh.exec_command('uptime')
    output=stdout.readlines()
    print(output)
    ssh.close()
    return

with open("nodelist2.txt") as input_file:
    for line in input_file:
        try:
            print("'{0}'".format(line.rstrip()))
            getuptime((line.rstrip()))
        except Exception as e:
            print()

