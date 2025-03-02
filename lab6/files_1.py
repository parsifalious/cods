import os 
path=input("write a path ").strip()
directories=[d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
all=os.listdir(path)
print("Directories:",directories)
print("Files",files)
print("All of them:",all)
# /Users/alialesov/Desktop/labs

