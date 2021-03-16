import logging
import argparse
import os
from collections import namedtuple
_ntuple_diskusage = namedtuple('usage', 'total used free')


def info_drive(drive_name):
    logger = logging.getLogger("info_drive")
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # Declaring variables for holding number of files and directory number.
    directory_number = files_number = 0
    for _, dirnames, filenames in os.walk(drive_name):
        files_number += len(filenames)
        directory_number += len(dirnames)
    logger.info("Drive name: " + drive_name)
    logger.info(f"Number of directories: {directory_number}")
    logger.info(f"Number of files: {files_number}")
    logger.info(disk_usage(drive_name))


def disk_usage(path):
    """Return disk usage statistics about the given path,
     Returned values is a named tuple with attributes 'total', 'used'
     and 'free', which are the amount of total, used and free space, in bytes."""
    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    return _ntuple_diskusage(total, used, free)

def switch_arguments(argument):
    switcher = {
        1: "-d"
    }
    print switcher.get(argument, "Use -d to get list of directories and number of files")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", help="list all the drives in a a machines")
    parser.add_argument("-h", help="Help Switch which will provide all possible switches and arguments")
    if (parser.parse_args().d):
        driver_name = parser.parse_args().d
        info_drive(driver_name)
    elif (parser.parse_args().h):
        help_name = parser.parse_args().h
        info_drive(help_name)