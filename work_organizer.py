import glob
import os
import shutil
import re
import calendar


def sorter(iteration):
    """
    Sorter is responsible for setting source and destination variables for files in drop folder
    """
    # Initializing year for non use.
    year = ""

    for file in glob.glob("*"):
        split_file = file.split(" ")
        if not os.path.isdir(file):
            # Initial iteration at scan and second iteration at Orders
            # Grab initial ref
            if (iteration == 0) or (iteration == 1):
                ref = split_file[0]
            # Iteration at check, grab name of carrier
            elif iteration == 2:
                ref = split_file[1]
            # Iteration at timesheet, grab name of driver
            elif iteration == 3:
                ref = "{0} {1}".format(split_file[2], split_file[3])
            # Iteration at receipts, grab month
            elif iteration == 4:
                # Will grab month from date on file name ex'['ER0001', '1-1-18']'
                date = split_file[1].split("-")
                year = "20" + date[2].split(".")[0]
                month = int(date[0])
                ref = calendar.month_name[month]

            else:
                return

            # Obtain realpath of current file for movement
            source = "{0}/{1}".format(os.path.dirname(os.path.realpath("__file__")), file)

            # sets Destination for file depending on Reference
            if iteration == 0:
                # only looking to match a six digit order number
                if re.match(r'^[0-9]{6,}', ref):
                    destination = "E:/Orders/{0}".format(file)
                # looking to match (ER****) for expense report
                elif re.match(r'^ER[0-9]{4,}', ref):
                    destination = "E:/Expense Report/{0}".format(file)
                else:
                    destination = "E:/{0}/{1}".format(ref, file)
            elif iteration == 4:
                destination = "{0}/{1}/{2}/{3}".format(os.path.dirname(os.path.realpath("__file__")), year, ref, file)
            else:
                destination = "{0}/{1}/{2}".format(os.path.dirname(os.path.realpath("__file__")), ref, file)

            # move file or create folder then move file
            mover(source, destination, ref, year)
            

def mover(source, destination, ref, year):
    """
    Mover uses pass variables to move files
    """
    # Move to corresponding parent folder
    if iteration == 0:
        shutil.move(source, destination)
    # When pertaining to Receipts or Expense reports.
    elif iteration == 4:
        # Check if year folder exists. If not, create it.
        if not os.path.exists(year):
            os.makedirs(year)
        # Check if month of year folder exists. If not, create it.
        if not os.path.exists(year + "/" + ref):
            os.makedirs(year + "/" + ref)
        # Move to year/month
        shutil.move(source, destination)
    else:
        # Check if folder for reference exists. If not create it.
        if not os.path.exists(ref):
            os.makedirs(ref)
        shutil.move(source, destination)

if __name__ == '__main__':
    iteration = 0

    # Start in Scan and move files to doc drive.
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
    iteration += 1

    # Move Receipts into specific Year/month folder
    os.chdir('E:/Receipts')
    sorter(iteration)