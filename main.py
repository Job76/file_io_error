import sys
import os
import shutil
import glob
import hashlib

# Does not support removal of folders beginning with a . (dot)
workdir = 'C:\\Users\\user\\OneDrive'
# filename = ''  # NON-DEFECTIVE
# filename = ''  # DEFECTIVE

os.chdir(workdir)
cwd = os.getcwd()
if workdir != cwd:  # Exit if not in the correct directory
    exit(1)
print(cwd)

overwrite = 1
mainfolder = os.getcwd()
# workfiles = glob.glob("**", recursive=True)
workfiles = glob.glob("**/*", recursive=True)
total_files = len(workfiles)
files_to_do = total_files
# print(files)
# print(workfiles)
print("Files found:", total_files)

hash_size = 1048576  # MD5 (first 1,048,576 bytes) 1048576 = 1024kb

if __name__ == '__main__':
    for file in workfiles:
        file_size = os.stat(file).st_size
        if file_size >= hash_size:
            read_size = hash_size
        else:
            read_size = file_size
        #  ===============================
        if os.path.isdir(file):
            if not os.listdir(file):
                print("Directory is empty:", file)
                os.rmdir(file)
            else:
                print("Directory is not empty")
        elif os.path.isfile(file):
            try:
                if os.path.exists(file) and os.path.isfile(file) and os.access(file, os.R_OK):
                    with open(file, 'rb') as f:
                        file_contents = f.read(read_size)
                    md5_result = hashlib.md5(file_contents)
                    print('File:', file)
                    print('MD5:', md5_result.hexdigest())
            except IOError:
                print("I/O Error: Could not read file:", file)
                # if file exists, delete it
                if os.path.isfile(file):
                    # try to delete the file
                    try:
                        print('Trying to remove file:', file)
                        os.remove(file)
                        pass
                    except OSError as e:
                        # If it fails, inform the user
                        print("Error: %s - %s." % (e.filename, e.strerror))
                else:
                    # If it fails, inform the user.
                    print("Error: File not found:", file)
            except OSError:
                print("Could not open/read file:", file)
            except Exception as err:
                print('There was some error in the file operations.')
                print(err)
                print(type(err).__name__)
        else:
            print("Given directory doesn't exist")
exit()
# End of File
