import os
products=["tomatoes","carrot","mayonase","chips","bread"]
file_path="output.txt"
with open(file_path,"w",encoding="utf-8") as file:
    for item in products:
        file.write(item+"\n")
