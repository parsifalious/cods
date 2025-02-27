import re
text=input()
x=re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()
print(x)
