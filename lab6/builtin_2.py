a=input()
low=0
up=0
for char in a:
    if char.islower():
        low+=1
for char in a:
    if char.isupper():
        up+=1
print("Uppercase letters:",up)
print("Lowercase letters:",low)
