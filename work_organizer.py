import glob
import os
import shutil
import re


def organizer(folder):
    if folder.lower() == "main":
        os.chdir('C:/Users/luisc/Documents/Scan')
    elif folder.lower() == "orders":
        os.chdir('E:/Orders')
    elif folder.lower() == "checks":
        os.chdir('E:/Checks')
    elif folder.lower() == "timesheets":
        os.chdir('E:/Timesheets')
    else:
        print ("that is not a valid option")
        return

    for file in glob.glob("*"):
        split_file = file.split(" ")
        if not os.path.isdir(file):
            if folder.lower() == "main":
                ref = split_file[0]
            elif folder.lower() == "orders":
                ref = split_file[0]
            elif folder.lower() == "checks":
                ref = split_file[1]
            elif folder.lower() == "timesheets":
                ref = "{0} {1}".format(split_file[1], split_file[2])
            else:
                print ("{0} {1}".format(file, "is not a valid file"))
                return

            source = "{0}/{1}".format(os.path.dirname(os.path.realpath("__file__")), file)
            print (source)
            if folder.lower() == "main":
                if re.match(r'^[0-9]\w', ref):
                    destination = "E:/Orders/{0}".format(file)
            else:    
                destination = "{0}/{1}/{2}".format(os.path.dirname(os.path.realpath("__file__")), ref, file)
                print (destination)    
            # move file or create folder then move file
            #if not re.match(r'^[0-9]\w', ref):
            if not os.path.exists(ref):
                os.makedirs(ref)
            shutil.move(source, destination)
            