import re
text=input()
x=re.sub("[ ,.]",":",text)
print(x)