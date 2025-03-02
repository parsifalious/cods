import os
file_path=input("write a file path")
if os.path.exists(file_path):
    if os.access(file_path,os.R_OK) and os.access(file_path,os.W_OK):
        os.remove(file_path)
        print("File is succesfully deleted")
    else:
        print("You dont have permission")
else:
    print("The file does not exist")