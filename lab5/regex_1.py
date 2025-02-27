import re
text=input()
x=re.search("^ab*$",text)
if x:
    print("Yes it matches")
else:
    print("No matches")