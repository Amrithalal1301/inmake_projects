import re
pattern="python"
if re.match(pattern,"python hello"):
    print("matched")
else :
    print("not matched")