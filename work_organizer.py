import glob
import os
import shutil
import re


def sorter(iteration):
    for file in glob.glob("*"):
        split_file = file.split(" ")
        if not os.path.isdir(file):
            if (iteration == 0) or (iteration == 1):
                ref = split_file[0]
            elif iteration == 2:
                ref = split_file[1]
            elif iteration == 3:
                ref = "{0} {1}".format(split_file[2], split_file[3])
            else:
                return

            source = "{0}/{1}".format(os.path.dirname(os.path.realpath("__file__")), file)

            if iteration == 0:
                if re.match(r'^[0-9]\w', ref):
                    destination = "E:/Orders/{0}".format(file)
                else:
                    destination = "E:/{0}/{1}".format(ref, file)
            else:
                destination = "{0}/{1}/{2}".format(os.path.dirname(os.path.realpath("__file__")), ref, file)

            # move file or create folder then move file
            if iteration == 0:
                shutil.move(source, destination)
            else:
                if not os.path.exists(ref):
                    os.makedirs(ref)
                shutil.move(source, destination)

if __name__ == '__main__':
    iteration = 0
    # Start in Scan and move to doc drive.
    os.chdir('C:/Users/luisc/Documents/Scan')
    sorter(iteration)
    iteration += 1    
    # Move to Orders into specific order folder
    os.chdir('E:/Orders')
    sorter(iteration)
    iteration += 1
    # Move Checks into specific company folder
    os.chdir('E:/Check')
    sorter(iteration)
    iteration += 1
    # Move Timesheets into specific driver folder
    os.chdir('E:/Timesheet')
    sorter(iteration)