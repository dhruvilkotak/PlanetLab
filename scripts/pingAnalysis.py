import re
import os


path = 'E:/mystuff/master/ccn/project2/allmergefiles/pingfiles'

for filename in os.listdir(path):
    print("node : "+filename)
    sum_of_stuff = dict()
    sum_of_stuff["min"] = 0.0
    sum_of_stuff["avg"] = 0.0
    sum_of_stuff["max"] = 0.0
    sum_of_stuff["mdev"] = 0.0

    count_of_stuff = 0

    with open(path+"/"+filename, "r") as ping_file:
        for line in ping_file:
            try:
                if "rtt min/avg/max/mdev" in line:
                    statment = line.split("=")
                    values = statment[1].split("/")

                    min = values[0]
                    avg = values[1]
                    max = values[2]
                    mdev = values[3].split("ms\n")[0]
                    sum_of_stuff["min"] += float(min)
                    sum_of_stuff["avg"] += float(avg)
                    sum_of_stuff["max"] += float(max)
                    count_of_stuff += 1
                    sum_of_stuff["mdev"] += float(mdev)
            except Exception as e:
                print(e)
                pass
    for (name, value) in sum_of_stuff.items():
        print("{} : {}".format(name, value / count_of_stuff))



