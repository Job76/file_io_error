import zipfile
import sys
import os
from os import path
import shutil
import glob
import time
from datetime import datetime
# import re
# import requests
import hashlib

backup = 'backup'
workdir = 'C:\\Users\\johan\\OneDrive (old-11GB)'
filename = '[text] bash for weldcam 1.txt'  # NON-DEFECTIVE
# filename = '[cheat sheet] Git - Atlassian.pdf'  # DEFECTIVE

os.chdir(workdir)
cwd = os.getcwd()
if workdir != cwd:  # Exit if not in the correct directory
    exit(1)
print(cwd)

overwrite = 1
mainfolder = os.getcwd()
workfiles = glob.glob("**", recursive=True)
total_files = len(workfiles)
files_to_do = total_files

# print(workfiles)
print("Files found:", total_files)

hash_size = 1048576  # MD5 (first 1,048,576 bytes) 1048576 = 1024kb

if __name__ == '__main__':
    file_size = os.stat(filename).st_size
    if file_size >= hash_size:
        read_size = hash_size
    else:
        read_size = file_size
    try:
        if os.path.exists(filename) and os.access(filename, os.R_OK):
            with open(filename, 'rb') as file:
                file_contents = file.read(read_size)
            print('\n\r')
            md5_result = hashlib.md5(file_contents)
            print('MD5:', md5_result.hexdigest())
    except IOError:
        print("I/O Error: Could not read file:", filename)
    except OSError():
        print("Could not open/read file:", filename)

exit()
# End of File
