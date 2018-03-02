import re
import os

path = 'E:/mystuff/master/ccn/project2/allmergefiles/traceroutefiles'
for filename in os.listdir(path):
    print("node : "+filename)
    lst_line = ""
    count_of_pats = 0
    count_of_stuff = 0
    preniment_failures = 0
    hopecount=0
    see_all = False
    flag=0
    count=0
    with open(path+"/"+filename, "r") as ping_file:



        for line in ping_file:
            # print(line[1], str.isdigit(line[1]))
            if str.isdigit(line[0]):
                count_of_pats += 1
            if "*" in line:
                count_of_stuff += 1
                # print(line)
                see_all = True
            if "BNM" in line:
                if "UCLA" not in lst_line:
                    preniment_failures += 1
                    #print(lst_line)
                    # if see_all:
                    # pass#print(line)
            lst_line = line

            if (line.split(" ")[0] == "traceroute"):
                flag = 1
                continue
            if (flag == 1 and len(line.strip()) != 0):
                count = count + 1
                if '*' in line:
                    count = count - 1
            if (len(line.strip()) == 0 and flag == 1):
                flag = 0
          #      print('count:', count)
                hopecount=hopecount+count
                count = 0

        # if count_of_stuff != 0:
       # print('hopecount=',hopecount)
       # print('*:',count_of_stuff )
        print('failure:',count_of_stuff/hopecount)
        if(count_of_stuff!=0):
            print("Temp : {} | Preme : {}".format((count_of_stuff - preniment_failures) / count_of_stuff,
                                              preniment_failures / count_of_stuff))