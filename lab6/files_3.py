import os
path =input("write a path ").strip()
if os.path.exists(path):
    print("path exists")
    directory = os.path.dirname(path)
    print("directory portion",directory)
    filename=os.path.basename(path)
    print("filename",filename)
else:
    print("PATH DOES NOT EXIST")



