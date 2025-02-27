import re
text=input()
x=re.search("^a.+b$",text)
if x:
    print("Yes it matches")
else:
    print("No matches")