import re

pattern = "[A-Z][1-9][a-z]"

if re.match(pattern,"P5nbgSdfghk"):
    print("Matched")
else:
    print("Not Matched!!!!")