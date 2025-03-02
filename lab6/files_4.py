import os
file_path=input("write a path")
if os.path.exists(file_path):
    with open (file_path,"r",encoding="utf-8") as file:
        line_count=sum(1 for line in file )
    print("The file has" ,line_count, "lines")
else:
    print("The file does not exists")
# '/Users/alialesov/Desktop/labs/lab6/Новая папка/Без названия.rtf'