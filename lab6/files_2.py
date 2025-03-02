import os
path=input("Write a path ").strip()
if os.path.exists(path):
    print("path exists")
    if os.access(path,os.R_OK):
        print("Path is readable")
    else:
        print("Path is not readble")
    if os.access(path,os.W_OK):
        print ("Path is writable")
    else:
        print("path is not writeable")
    if os.access(path, os.X_OK):
        print("path is executable")
    else:
        print("path is not executable")
