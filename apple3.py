import re

s = "AFB+8HC-4AFB+8SC-4H-2GDPE+9"

def eggrolls(s):
    pattern = "([A-T]+[\+\-][1-9])"
    result = re.findall(pattern, s)
    print(result)
    for a in result:
        print(a.replace("+", " tighten ").replace("-", " loosen "))
    if pattern repeats?

eggrolls(s)


