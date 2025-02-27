import re
text=input()
x=re.search("^[a-z]+_[a-z]",text)
if x:
    print("Yes it matches")
else:
    print("No matches")
