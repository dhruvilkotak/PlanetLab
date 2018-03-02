import re
import os

path = 'E:/mystuff/master/ccn/project2/allmergefiles/traceroutefiles'
changed=0
for filename in os.listdir(path):
    print("node : "+filename)
    count=0
    flag=0
    flag1=0
    with open(path+"/"+filename, "r") as ping_file:
        count1 = 0
        for line in ping_file:
            # print(line[1], str.isdigit(line[1]))
            if (line.split(" ")[0] == "traceroute"):
                flag = 1
                continue
            if (flag == 1 and len(line.strip()) != 0):
                count = count + 1
                if '*' in line:
                    count=count-1
            if (len(line.strip()) == 0 and flag == 1):
                flag = 0
                #print('count:',count)
                if(count1!=count and count1!=0):
                    if(flag1==0):
                        print("hope changed in:",filename)
                        print("from count:",count1,' to count:',count)
                        changed=changed+1
                        flag1=1
                count1=count
                count = 0
print('changed:',changed)