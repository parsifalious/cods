import re
text=input()
x=re.search("^[A-Z][a-z]",text)
if x:
    print("Yes it matches")
else:
    print("No matches")

