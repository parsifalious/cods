import re 
text = input()
x=re.search("^ab{2,3}$",text)
if x:
    print("Yes it matches")
else:
    print("No matches")
