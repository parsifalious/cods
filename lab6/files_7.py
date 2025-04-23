import os 
with open('source.txt', 'r') as source_file:
    with open('destination.txt', 'w') as destination_file:
        destination_file.write(source_file.read())

print("File copied successfully.")
