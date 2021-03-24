import logging
import argparse
import os
from datetime import datetime
from collections import namedtuple
_ntuple_diskusage = namedtuple('usage', 'total used free')

# info -d method
def info_drive(drive_name):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='project_1.log')
    console = logging.StreamHandler() # Setting up logging to console
    console.setLevel(logging.INFO) # to display info messages in console
    logging.getLogger('').addHandler(console) # Add the handler to the root logger
    logging.info(datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + " Drive name: " + drive_name)
    logging.info(disk_usage(drive_name))
    # Declaring variables for holding number of files and directory number.
    directory_number = files_number = 0
    for _, dirnames, filenames in os.walk(drive_name):
                files_number += len(filenames)
                directory_number += len(dirnames)
    # Generating time stamps for log files
    logging.info(datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + f"Number of directories: {directory_number}")
    logging.info(datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + f"Number of files: {files_number}")

# method to see how much available, used and free storage is there
def disk_usage(path):
    """Return disk usage statistics about the given path,
     Returned values is a named tuple with attributes 'total', 'used'
     and 'free', which are the amount of total, used and free space, in bytes."""
    try:
        st = os.statvfs(path) # statvfs perform statvfs system call on the given path.
        free = st.f_bavail * st.f_frsize # free number of blocks file in a block system
        total = st.f_blocks * st.f_frsize # total number of blocks in a file system
        used = (st.f_blocks - st.f_bfree) * st.f_frsize # used number of blocks in a file system
        return _ntuple_diskusage(total, used, free)
    except FileNotFoundError as fe:
        logging.warning(str(fe))
    except Exception as e:
        logging.critical(str(e))


# main method

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Help switch which will provide all possible switches and arguments
    parser.add_argument("-d", help="list all the drives in a a machines")
    parser.add_argument("-l", help="To list all the folders in a given drive")
    parser.add_argument("-f", help="To list all the files of the machine")
    parser.add_argument("-t", help="To list all the types of files exist in machine")


    # optional argument -d

    if (parser.parse_args().d):
        driver_name = parser.parse_args().d
        info_drive(driver_name)
