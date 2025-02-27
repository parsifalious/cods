import re
text=input()
x=re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
print(x)