import paramiko
import time

def getPingtrace(x,y):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(x,username='albany_ccn1',password='12345')
    stdin,stdout,stderr=ssh.exec_command('ping '+y+' -c 20')
    output=stdout.readlines()
    stdin2, stdout2, stderr2 = ssh.exec_command('traceroute ' + y)
    output2 = stdout2.readlines()
    ssh.close()
    return output,output2

def pingFile(filename):
    f = open("nodelist.txt")
    content = f.readlines()
    i=0
    while (i+1 < len(content)):
        try:
            f1 = open('ping_' + content[i].rstrip() , 'a+')
            f2 = open('traceroute_' + content[i].rstrip(), 'a+')
            f3 = open('ping_' +content[i+1].rstrip(), 'a+')
            f4 = open('traceroute_' + content[i+1].rstrip(), 'a+')
            f1.write('\n'+time.strftime("%Y%m%d-%H%M%S")+'\n')
            f2.write('\n'+ time.strftime("%Y%m%d-%H%M%S")+'\n')
            f3.write('\n'+ time.strftime("%Y%m%d-%H%M%S")+'\n')
            f4.write('\n'+ time.strftime("%Y%m%d-%H%M%S")+'\n')
            x=content[i].rstrip()
            y=content[i+1].rstrip()
            output1,output2=getPingtrace(x,y)
            f1.write(''+" ".join(str(l) for l in output1))
            f2.write('' + " ".join(str(l) for l in output2))
            output1, output2 = getPingtrace(y,x)
            f3.write('' + " ".join(str(l) for l in output1))
            f4.write('' + " ".join(str(l) for l in output2))
            f1.close()
            f2.close()
            f3.close()
            f4.close()
            i=i+2;
        except Exception as e:
                print(e)
                i = i + 2;
    time.sleep(45*60)
    return

while True:
    print(time.strftime("%Y%m%d-%H%M%S"))
    pingFile(time.strftime("%Y%m%d-%H%M%S"))
